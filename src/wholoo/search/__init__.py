# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.search.models import SearchModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())

# The discover search endpoint. A plain REST GET on ``discover.hulu.com`` that
# returns entity search results grouped by category (``top results`` etc.).
_SEARCH_URL = "https://discover.hulu.com/content/v5/search/entity"


class Search(BaseEndpoint[SearchModel]):
    """Manage the search file.

    Wraps ``GET https://discover.hulu.com/content/v5/search/entity``, the query
    that backs Hulu's search page.
    """

    _response_model = SearchModel

    def get_log_id(self, query: str) -> str:
        """Build the log id for a download."""
        return f"{self.__class__.__name__} {query=}"

    @staticmethod
    def _params(query: str, limit: int, *, include_offsite: bool) -> dict[str, str]:
        return {
            "language": "en",
            "device_context_id": "2",
            "search_query": query,
            "keywords": query,
            "type": "entity",
            "limit": str(limit),
            "include_offsite": "true" if include_offsite else "false",
            "schema": "3",
            "device_info": "web:4.44.1",
            "referralHost": "production",
        }

    def download(
        self,
        query: str,
        *,
        limit: int = 64,
        include_offsite: bool = True,
    ) -> dict[str, Any]:
        """Downloads the entity search results for a query.

        Args:
            query: The search text, e.g. ``"bob's burgers"``.
            limit: The maximum number of results to return (default ``64``).
            include_offsite: Whether to include titles that are not streamable on
                Hulu itself (default ``True``), mirroring the web player.
        """
        return self._client.download(
            _SEARCH_URL,
            referer="https://www.hulu.com/search",
            params=self._params(query, limit, include_offsite=include_offsite),
            log_id=self.get_log_id(query),
        )

    def download_and_parse(
        self,
        query: str,
        *,
        limit: int = 64,
        include_offsite: bool = True,
    ) -> SearchModel:
        """Downloads and parses the entity search results for a query."""
        return self.parse(
            self.download(query, limit=limit, include_offsite=include_offsite),
        )
