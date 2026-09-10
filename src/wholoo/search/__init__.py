from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.exceptions import WholooError
from wholoo.search.models import SearchModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


def extract_search(response: str) -> dict[str, Any]:
    """Extract the search results from the Search response."""
    if groups := json.loads(response)["groups"]:
        return groups[0]

    # This is an error because Hulu always returns results even for nonsensical queries.
    msg = "The response has no search results in it"
    raise WholooError(msg)


class Search(BaseEndpoint):
    """Contains the titles a search matches.

    - Example Request:
        - URL: https://www.hulu.com/search?q=poopy

        - Headers:
            - GET /content/v5/search/entity?
                - language=en&
                - device_context_id=2&
                - search_query=poopy&
                - limit=64&
                - include_offsite=true&
                - v=__REDACTED__&
                - schema=3&
                - device_info=web:4.46.0&
                - referralHost=production&
                - keywords=poopy&
                - type=entity&
                - limit=64
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

    def __call__(
        self,
        query: str,
        *,
        include_offsite: bool = True,
    ) -> SearchModel:
        """Download and parse the Search file."""
        log_id = self.get_log_id(self.__call__, locals())
        download_response = self.download(query, include_offsite=include_offsite)
        return self.load(download_response, log_id)

    def download(
        self,
        query: str,
        *,
        include_offsite: bool = True,
    ) -> str:
        """Download the Search file."""
        log_id = self.get_log_id(self.download, locals())
        params = [
            ("language", "en"),
            ("device_context_id", "2"),
            ("search_query", query),
            ("limit", "64"),
            ("include_offsite", str(include_offsite).lower()),
            # The site also sends a `v` UUID, which may or may not be private.
            ("schema", "3"),
            ("device_info", "web:4.44.1"),
            ("referralHost", "production"),
            ("keywords", query),
            ("type", "entity"),
            # Hulu.com sends the parameter twice so Wholoo sends it twice too.
            ("limit", "64"),
        ]
        return self._client.download(
            endpoint="content/v5/search/entity",
            params=params,
            headers={"Referer": "https://www.hulu.com/search"},
            log_id=log_id,
        )

    def load(self, data: str, log_id: str = "") -> SearchModel:
        """Load a Search file into its model."""
        return model_validate_json(extract_search(data), log_id or self.default_log_id)
