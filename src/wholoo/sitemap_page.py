# TODO: Validate
"""Contains the SitemapPage class."""

from __future__ import annotations

import re
from logging import NullHandler, getLogger

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
class SitemapPage(BaseEndpoint):
    """Base class for one page of the sitemap.

    A sitemap page is served as HTML rather than through the API, so what is
    downloaded is the page data out of it and the markup around it is dropped.

    Source: https://www.hulu.com/sitemap/{path}
    """

    # TODO: Validate
    def _download(self, path: str, log_id: str) -> str:
        """Download one sitemap page and return the page data it carries.

        Raises:
            PageDataError: If the page carries no page data.
        """
        html = self._client.download_page(f"sitemap/{path}", log_id)
        page_data = PAGE_DATA.search(html)
        if page_data is None:
            msg = f"No page data found in the page downloaded for {log_id}"
            raise PageDataError(msg)
        return page_data.group(1)
