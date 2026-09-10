from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.all_series.models import AllSeriesModel, model_validate_json
from wholoo.sitemap_page import SitemapPage, extract_list_card

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class AllSeries(SitemapPage):
    """Contains information about all* of the series on Hulu.

    Named AllSeries because the page header says "All Series".

    *Not really all of the series even though Hulu claims it is all of them.

    - Example Request:
        - URL: https://www.hulu.com/sitemap/series

        - Headers:
            - GET /sitemap/series HTTP/2
            - Host: www.hulu.com
            - User-Agent: __REDACTED__
            - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
            - Accept-Language: en-US,en;q=0.9
            - Accept-Encoding: gzip, deflate, br, zstd
            - Upgrade-Insecure-Requests: 1
            - Sec-Fetch-Dest: document
            - Sec-Fetch-Mode: navigate
            - Sec-Fetch-Site: none
            - Sec-Fetch-User: ?1
            - Connection: keep-alive
            - Cookie: __REDACTED__
            - Priority: u=0, i
            - TE: trailers
    """

    def __call__(self) -> AllSeriesModel:
        """Download and parse the AllSeries file."""
        return self.load(self.download(), self.default_log_id)

    def download(self) -> str:
        """Download the AllSeries file."""
        return self._download("series", self.default_log_id)

    def load(self, data: str, log_id: str = "") -> AllSeriesModel:
        """Load an AllSeries file into its model."""
        return model_validate_json(
            extract_list_card(data),
            log_id or self.default_log_id,
        )
