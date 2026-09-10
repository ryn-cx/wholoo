from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.all_movies.models import AllMoviesModel, model_validate_json
from wholoo.sitemap_page import SitemapPage, extract_list_card

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class AllMovies(SitemapPage):
    """Contains information about all* of the movies on Hulu.

    Named AllMovies because the page header says "All Movies".

    *Not really all of the movies even though Hulu claims it is all of them.

    - Example Request:
        - URL: https://www.hulu.com/sitemap/movies

        - Headers:
            - GET /sitemap/movies HTTP/2
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

    def __call__(self) -> AllMoviesModel:
        """Download and parse the AllMovies file."""
        return self.load(self.download(), self.default_log_id)

    def download(self) -> str:
        """Download the AllMovies file."""
        return self._download("movies", self.default_log_id)

    def load(self, data: str, log_id: str = "") -> AllMoviesModel:
        """Load an AllMovies file into its model."""
        return model_validate_json(
            extract_list_card(data),
            log_id or self.default_log_id,
        )
