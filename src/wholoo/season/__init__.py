from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.exceptions import ResourceNotFoundError, SeasonNotFoundError
from wholoo.season.models import SeasonModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Season(BaseEndpoint):
    """Contains the episodes of one season.

    - Example Request:
        - URL: https://www.hulu.com/series/f089664b-1a87-433b-86a5-24e7da5a246a

        - Headers:
            - GET /content/v5/hubs/series/f089664b-1a87-433b-86a5-24e7da5a246a
              /season/3?
                - limit=1999&
                - schema=3&
                - personalized_layout_id=__REDACTED__&
                - offset=0&
                - device_info=web:4.46.0&
                - referralHost=production
                - HTTP/1.1
            - Host: discover.hulu.com
            - User-Agent: __REDACTED__
            - Accept: */*
            - Accept-Language: en-US,en;q=0.9
            - Accept-Encoding: gzip, deflate, br, zstd
            - Referer: https://www.hulu.com/
            - Origin: https://www.hulu.com
            - Sec-Fetch-Dest: empty
            - Sec-Fetch-Mode: cors
            - Sec-Fetch-Site: same-site
            - Connection: keep-alive
            - Cookie: __REDACTED__
            - Priority: u=0
    """

    def __call__(
        self,
        series_id: str,
        season: int,
        *,
        offset: int = 0,
    ) -> SeasonModel:
        """Download and parse the Season file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id, season, offset=offset), log_id)

    def download(
        self,
        series_id: str,
        season: int,
        *,
        offset: int = 0,
    ) -> str:
        """Download the Season file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"content/v5/hubs/series/{series_id}/season/{season}",
                params={
                    "schema": "3",
                    "limit": "1999",
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
        return response

    def load(self, data: str, log_id: str = "") -> SeasonModel:
        """Load a Season file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
