# TODO: Validate
"""Contains the Genre class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.exceptions import GenreNotFoundError, ResourceNotFoundError
from wholoo.genre.models import GenreModel, model_validate_json
from wholoo.sitemap_page import SitemapPage

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Genre(SitemapPage):
    """Manage one genre's title list file.

    The page lists every series and movie the genre holds, each as the name it
    is shown under and the path to its details page.

    Source: https://www.hulu.com/sitemap/genres/{genre_id}

    Example request:
        - GET /sitemap/genres/{genre_id} HTTP/2
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
    def __call__(self, genre_id: str) -> GenreModel:
        """Look one genre's titles up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(genre_id), log_id)

    # TODO: Validate
    def download(self, genre_id: str) -> str:
        """Download one genre's title list file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(f"genres/{genre_id}", log_id)
        except ResourceNotFoundError as err:
            raise GenreNotFoundError(genre_id, err.status_code, err.response) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> GenreModel:
        """Read a downloaded genre title list file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
