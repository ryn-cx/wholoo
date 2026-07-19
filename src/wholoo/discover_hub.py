# TODO: Validate
"""Shared base for ``discover.hulu.com`` content-hub endpoints."""

from __future__ import annotations

import random
from typing import Any, ClassVar

from good_ass_pydantic_integrator import GAPIBaseModel

from wholoo.base_api_endpoint import BaseEndpoint

# The discover content API that backs a title's details page. A plain REST GET on
# ``discover.hulu.com`` that returns the full, unfiltered details hub. The
# ``{content_type}`` segment is ``movie`` or ``series``.
_HUB_URL = "https://discover.hulu.com/content/v5/hubs/{content_type}/{content_id}"


class DiscoverHubEndpoint[T: GAPIBaseModel](BaseEndpoint[T]):
    """Base for a ``discover.hulu.com/content/v5/hubs/<type>/<id>`` endpoint.

    Subclasses set :attr:`_content_type` (``"movie"`` / ``"series"``) and
    :attr:`_response_model`.
    """

    _content_type: ClassVar[str]

    def get_log_id(self, content_id: str) -> str:
        """Build the log id for a download."""
        return f"{self.__class__.__name__} {content_id=}"

    @staticmethod
    def _params(cache_key: str) -> dict[str, str]:
        return {
            "schema": "3",
            "limit": "1999",
            "device_info": "web:4.44.1",
            "referralHost": "production",
            "cacheKey": cache_key,
            "pageType": "DETAILS",
        }

    def download(
        self,
        content_id: str,
        *,
        cache_key: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the details hub file.

        Args:
            content_id: The Hulu title id, e.g.
                ``"4ee4f57e-19bd-493f-96f9-ad3e753af981"``.
            cache_key: The ``cacheKey`` cache-buster the query param carries. A
                random value is generated when omitted, mirroring the web player.
        """
        if cache_key is None:
            cache_key = str(random.random())  # noqa: S311 - cache-buster, not crypto.
        url = _HUB_URL.format(content_type=self._content_type, content_id=content_id)
        referer = f"https://www.hulu.com/{self._content_type}/{content_id}"
        return self._client.download(
            url,
            referer=referer,
            params=self._params(cache_key),
            log_id=self.get_log_id(content_id),
        )

    def download_and_parse(self, content_id: str) -> T:
        """Downloads and parses the details hub file."""
        return self.parse(self.download(content_id))
