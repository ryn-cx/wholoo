"""Contains the Genres class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.genres.models import GenresModel, model_validate_json
from wholoo.sitemap_page import SitemapPage, extract_list_card

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Genres(SitemapPage):
    """Contains every genre the site has a sitemap page for.

    - Example Request:
        - URL: https://www.hulu.com/sitemap/genres

        - Headers:
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

    def __call__(self) -> GenresModel:
        """Download and parse the Genres file."""
        return self.load(self.download(), self.default_log_id)

    def download(self) -> str:
        """Download the Genres file."""
        return self._download("genres", self.default_log_id)

    def load(self, data: str, log_id: str = "") -> GenresModel:
        """Load a Genres file into its model."""
        return model_validate_json(
            extract_list_card(data),
            log_id or self.default_log_id,
        )
