from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.exceptions import GenreNotFoundError, ResourceNotFoundError
from wholoo.genre.models import GenreModel, model_validate_json
from wholoo.sitemap_page import SitemapPage, extract_list_card

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Genre(SitemapPage):
    """Contains titles.

    - Example Request:
        - URL: www.hulu.com/sitemap/genres/latino-movies

        - Headers:
            - GET /sitemap/genres/latino-movies HTTP/2
            - Host: www.hulu.com
            - User-Agent: __REDACTED__
            - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
            - Accept-Language: en-US,en;q=0.9
            - Accept-Encoding: gzip, deflate, br, zstd
            - Upgrade-Insecure-Requests: 1
            - Sec-Fetch-Dest: document
            - Sec-Fetch-Mode: navigate
            - Sec-Fetch-Site: none
            - Connection: keep-alive
            - Cookie: __REDACTED__
            - Priority: u=0, i
            - TE: trailers
    """

    # TODO: Validate
    def __call__(self, genre_id: str) -> GenreModel:
        """Download and parse the Genre file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(genre_id), log_id)

    def download(self, genre_id: str) -> str:
        """Download the Genre file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(f"genres/{genre_id}", log_id)
        except ResourceNotFoundError as err:
            raise GenreNotFoundError(genre_id, err.status_code, err.response) from err

    def load(self, data: str, log_id: str = "") -> GenreModel:
        """Load a Genre file into its model."""
        return model_validate_json(
            extract_list_card(data),
            log_id or self.default_log_id,
        )
