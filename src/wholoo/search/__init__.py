# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.search.models import SearchModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Search(BaseEndpoint):
    """Manage the search file.

    Source: https://www.hulu.com/search?q={query}

    Example request:
        - GET /content/v5/search/entity?
            - language=en&
            - device_context_id=2&
            - search_query={query}&
            - limit=64&
            - include_offsite=true&
            - schema=3&
            - device_info=web:4.44.1&
            - referralHost=production&
            - keywords={query}&
            - type=entity&
            - limit=64
            - HTTP/2
        - Host: discover.hulu.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.hulu.com/search
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
        query: str,
        *,
        limit: int = 64,
        include_offsite: bool = True,
    ) -> SearchModel:
        """Run the search and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(query, limit=limit, include_offsite=include_offsite),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        query: str,
        *,
        limit: int = 64,
        include_offsite: bool = True,
    ) -> str:
        """Download the search file."""
        log_id = self.get_log_id(self.download, locals())
        params = [
            ("language", "en"),
            ("device_context_id", "2"),
            ("search_query", query),
            ("limit", str(limit)),
            ("include_offsite", str(include_offsite).lower()),
            # The site also sends a `v` UUID, which may or may not be private.
            ("schema", "3"),
            ("device_info", "web:4.44.1"),
            ("referralHost", "production"),
            ("keywords", query),
            ("type", "entity"),
            # The site sends limit twice, and so does this.
            ("limit", str(limit)),
        ]
        return self._client.download(
            endpoint="content/v5/search/entity",
            params=params,
            headers={"Referer": "https://www.hulu.com/search"},
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SearchModel:
        """Read a downloaded search file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
