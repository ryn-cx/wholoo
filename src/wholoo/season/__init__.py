# TODO: Validate
"""Contains the Season class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.exceptions import ResourceNotFoundError, SeasonNotFoundError
from wholoo.season.models import SeasonModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

LIMIT = 1999


# TODO: Validate
class Season(BaseEndpoint):
    """Manage the season episodes file.

    The series details file is a hub listing the seasons, while this is a
    collection whose items are one season's episodes.

    Source: https://www.hulu.com/series/{series_id}

    Example request:
        - GET /content/v5/hubs/series/{series_id}/season/{season}?
            - schema=3&
            - limit=1999&
            - offset=0&
            - device_info=web:4.44.1&
            - referralHost=production
            - HTTP/2
        - Host: discover.hulu.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.hulu.com/series/{series_id}
        - Origin: https://www.hulu.com
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-site
        - Connection: keep-alive
        - Cookie: __REDACTED__
        - Priority: u=4
    """

    # TODO: Validate
    def __call__(
        self,
        series_id: str,
        season: int,
        *,
        offset: int = 0,
        limit: int = LIMIT,
    ) -> SeasonModel:
        """Look one season's episodes up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(series_id, season, offset=offset, limit=limit),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        series_id: str,
        season: int,
        *,
        offset: int = 0,
        limit: int = LIMIT,
    ) -> str:
        """Download the season episodes file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"content/v5/hubs/series/{series_id}/season/{season}",
                params={
                    "schema": "3",
                    "limit": str(limit),
                    "offset": str(offset),
                    "device_info": "web:4.44.1",
                    "referralHost": "production",
                },
                headers={"Referer": f"https://www.hulu.com/series/{series_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonNotFoundError(
                series_id,
                season,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, series_id, season)

    # TODO: Validate
    def _validate_download(self, response: str, series_id: str, season: int) -> str:
        """Check that the collection holds episodes.

        A season a real series does not have is answered with an empty
        collection rather than with an error.
        """
        # TODO: There is no way to tell the difference between a season that used to
        # exist and was deleted and a season that is invalid.
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SeasonModel:
        """Read a downloaded season episodes file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
