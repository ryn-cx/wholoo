"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.search.models import SearchModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Search(BaseEndpoint[SearchModel, [str]]):
    """Wraps `GET https://discover.hulu.com/content/v5/search/entity`.

    Source: Returned when searching at https://www.hulu.com/search (must be logged in).

    Example request headers:
    - GET /content/v5/search/entity?
        - language=en
        - device_context_id=2
        - search_query=SEARCH_TERM
        - limit=64
        - include_offsite=true
        - v=__REDACTED__
            - This was a UUID, not sure waht it does so it was redacted just in
                case.
        - schema=3
        - device_info=web:4.44.1
        - referralHost=production
        - keywords=SEARCH_TERM
        - type=entity
        - limit=64
        - HTTP/2
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

    _response_model = SearchModel

    @override
    def download(
        self,
        query: str,
        *,
        limit: int = 64,
        include_offsite: bool = True,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())


        params = (
            ("language", "en"),
            ("device_context_id", "2"),
            ("search_query", query),
            ("limit", str(limit)),
            ("include_offsite", "true" if include_offsite else "false"),
            # ("v", ...), The client sends a UUID which may or may not be private.
            ("schema", "3"),
            ("device_info", "web:4.44.1"),
            ("referralHost", "production"),
            ("keywords", query),
            ("type", "entity"),
            # Limit is duplicated intentionally to match the real request.
            ("limit", str(limit)),
        )

        return self._client.download(
            "https://discover.hulu.com/content/v5/search/entity",
            referer="https://www.hulu.com/search",
            params=params,
            log_id=log_id,
        )

    @override
    def download_and_parse(
        self,
        query: str,
        *,
        limit: int = 64,
        include_offsite: bool = True,
    ) -> SearchModel:
        return self.parse(
            self.download(query, limit=limit, include_offsite=include_offsite),
        )
