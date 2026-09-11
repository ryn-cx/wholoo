from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from wholoo.discover_hub import DiscoverHub
from wholoo.exceptions import MovieNotFoundError
from wholoo.movies.models import MoviesModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def _validate_download(response: str, content_id: str) -> str:
    if not json.loads(response)["details"].get("entity"):
        raise MovieNotFoundError(content_id, HTTPStatus.OK, response)
    return response


class Movies(DiscoverHub):
    """Contains information about a specific movie.

    - Example Request:
        - URL: https://www.hulu.com/movie/0957a9a1-015a-4bbf-913b-9da75572bb8d

        - Headers:
            - GET /content/v5/hubs/movie/0957a9a1-015a-4bbf-913b-9da75572bb8d?
                - schema=3&
                - limit=1999&
                - device_info=web:4.46.0&
                - referralHost=production&
                - cacheKey=0.31194440120842093&
                - pageType=DETAILS
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
            - Priority: u=4
    """

    def __call__(self, content_id: str) -> MoviesModel:
        """Download and parse the Movies file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(content_id), log_id)

    def download(self, content_id: str) -> str:
        """Download the Movies file."""
        log_id = self.get_log_id(self.download, locals())
        response = self._download("movie", content_id, 1999, log_id)
        return _validate_download(response, content_id)

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MoviesModel:
        """Load a Movies file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
