# TODO: Validate
"""Contains the Genres class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.genres.models import GenresModel, model_validate_json
from wholoo.sitemap_page import SitemapPage

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Genres(SitemapPage):
    """Manage the genre list file.

    The page lists every genre the site has a sitemap page for.

    Source: https://www.hulu.com/sitemap/genres

    Example request:
        - GET /sitemap/genres HTTP/2
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
    def __call__(self) -> GenresModel:
        """Look the genre list up and return the model it is read into."""
        return self.load(self.download(), self.default_log_id)

    # TODO: Validate
    def download(self) -> str:
        """Download the genre list file."""
        return self._download("genres", self.default_log_id)

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> GenresModel:
        """Read a downloaded genre list file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
