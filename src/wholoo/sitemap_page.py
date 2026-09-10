# TODO: Validate
"""Contains the SitemapPage class."""

from __future__ import annotations

import json
import re
from logging import NullHandler, getLogger
from typing import Any

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.exceptions import PageDataError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PAGE_DATA = re.compile(
    r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
    re.DOTALL,
)
"""The JSON every hulu.com page carries the data it renders in."""


# TODO: Validate
def extract_list_card(page_data: str) -> dict[str, Any]:
    """Extract the list_card from the sitemap page response."""
    components = json.loads(page_data)["props"]["pageProps"]["layout"]["components"]
    return next(
        component for component in components if component["type"] == "list_card"
    )


# TODO: Validate
class SitemapPage(BaseEndpoint):
    """Base class for one page of the sitemap.

    A sitemap page is served as HTML rather than through the API, so what is
    downloaded is the page data out of it.

    - Example Request:
        - URL: https://www.hulu.com/sitemap/{path}
    """

    # TODO: Validate
    def _download(self, path: str, log_id: str) -> str:
        """Download one sitemap page and return the page data it carries."""
        html = self._client.download_page(f"sitemap/{path}", log_id)
        page_data = PAGE_DATA.search(html)
        if page_data is None:
            msg = f"No page data found in the page downloaded for {log_id}"
            raise PageDataError(msg)
        return page_data.group(1)
