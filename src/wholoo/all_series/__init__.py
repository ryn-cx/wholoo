# TODO: Validate
"""Contains the AllSeries class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.all_series.models import AllSeriesModel, model_validate_json
from wholoo.sitemap_page import SitemapPage

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class AllSeries(SitemapPage):
    """Manage the series list file.

    The page lists every series the site has, each as the name it is shown under
    and the path to its details page.

    Source: https://www.hulu.com/sitemap/series

    Example request:
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
        - Priority: u=0, i
    """

    # TODO: Validate
    def __call__(self) -> AllSeriesModel:
        """Look the series list up and return the model it is read into."""
        return self.load(self.download(), self.default_log_id)

    # TODO: Validate
    def download(self) -> str:
        """Download the series list file."""
        return self._download("series", self.default_log_id)

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> AllSeriesModel:
        """Read a downloaded series list file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
