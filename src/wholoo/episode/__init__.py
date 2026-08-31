# TODO: Validate
"""Contains the Episode class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.episode.models import EpisodeModel, model_validate_json
from wholoo.exceptions import EpisodeNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

LIMIT = 1999


# TODO: Validate
class Episode(BaseEndpoint):
    """Manage the episode details file.

    It is the only place the id of the series an episode belongs to can be
    looked up.

    Source: https://www.hulu.com/watch/{episode_id}

    Example request:
        - GET /content/v5/hubs/episode/{episode_id}?
            - schema=3&
            - limit=1999&
            - device_info=web:4.44.1&
            - referralHost=production&
            - pageType=DETAILS
            - HTTP/2
        - Host: discover.hulu.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.hulu.com/watch/{episode_id}
        - Origin: https://www.hulu.com
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-site
        - Connection: keep-alive
        - Cookie: __REDACTED__
        - Priority: u=4
    """

    # TODO: Validate
    def __call__(self, episode_id: str, *, limit: int = LIMIT) -> EpisodeModel:
        """Look the episode up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(episode_id, limit=limit), log_id)

    # TODO: Validate
    def download(self, episode_id: str, *, limit: int = LIMIT) -> str:
        """Download the episode details file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"content/v5/hubs/episode/{episode_id}",
                params={
                    "schema": "3",
                    "limit": str(limit),
                    "device_info": "web:4.44.1",
                    "referralHost": "production",
                    "pageType": "DETAILS",
                },
                headers={"Referer": f"https://www.hulu.com/watch/{episode_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise EpisodeNotFoundError(
                episode_id,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, episode_id)

    # TODO: Validate
    def _validate_download(self, response: str, episode_id: str) -> str:
        """Check that the hub describes an episode.

        An id nothing is under is answered with a 200 carrying a hub that has
        no entity in it.
        """
        if not json.loads(response).get("details", {}).get("entity"):
            raise EpisodeNotFoundError(episode_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> EpisodeModel:
        """Read a downloaded episode details file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
