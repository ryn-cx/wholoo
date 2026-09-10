from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.episode.models import EpisodeModel, model_validate_json
from wholoo.exceptions import EpisodeNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


def extract_episode(response: str) -> dict[str, Any]:
    """Extract the episode from the Episode response."""
    return json.loads(response)["details"]


def _validate_download(response: str, episode_id: str) -> str:
    # A correctly formatted but invalid episode_id will return a success with no
    # entity.
    if not extract_episode(response).get("entity"):
        raise EpisodeNotFoundError(episode_id, HTTPStatus.OK, response)
    return response


class Episode(BaseEndpoint):
    """Contains information about a specific episode.

    # TODO: What is the origin of this request? It may have just been bruteforced based
    on the format of the other endpoints.
    """

    def __call__(self, episode_id: str) -> EpisodeModel:
        """Download and parse the Episode file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(episode_id), log_id)

    def download(self, episode_id: str) -> str:
        """Download the Episode file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"content/v5/hubs/episode/{episode_id}",
                params={
                    "schema": "3",
                    "limit": "1999",
                    "device_info": "web:4.44.1",
                    "referralHost": "production",
                    "pageType": "DETAILS",
                },
                headers={"Referer": f"https://www.hulu.com/watch/{episode_id}"},
                log_id=log_id,
            )
        # A malformed episode_id will return a 404 error.
        except ResourceNotFoundError as err:
            raise EpisodeNotFoundError(
                episode_id,
                err.status_code,
                err.response,
            ) from err
        return _validate_download(response, episode_id)

    def load(self, data: str, log_id: str = "") -> EpisodeModel:
        """Load an Episode file into its model."""
        return model_validate_json(extract_episode(data), log_id or self.default_log_id)
