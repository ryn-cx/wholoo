from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from time import monotonic, sleep
from typing import TYPE_CHECKING

from get_around import GetAround

from wholoo.all_movies import AllMovies
from wholoo.all_series import AllSeries
from wholoo.episode import Episode
from wholoo.exceptions import CookieError, HTTPError, ResourceNotFoundError
from wholoo.genre import Genre
from wholoo.genres import Genres
from wholoo.movies import Movies
from wholoo.search import Search
from wholoo.season import Season
from wholoo.tv import TV

if TYPE_CHECKING:
    from collections.abc import Mapping

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_DOMAIN = "discover.hulu.com"
WEB_ORIGIN = "https://www.hulu.com"

type Params = Mapping[str, str] | list[tuple[str, str]]
"""Query parameters, as a mapping or as pairs when a name is repeated."""


class Wholoo:
    """Hulu API wrapper."""

    def __init__(
        self,
        get_around_client: GetAround | None = None,
        sleep_time: float = 0,
    ) -> None:
        """Initialize the Wholoo client."""
        self.get_around_client = get_around_client or GetAround()
        self.sleep_time = sleep_time
        self._cookie_value = ""

        self.movies = Movies(self)
        self.tv = TV(self)
        self.season = Season(self)
        self.episode = Episode(self)
        self.search = Search(self)
        self.genres = Genres(self)
        self.genre = Genre(self)
        self.all_series = AllSeries(self)
        self.all_movies = AllMovies(self)

    @property
    def _cookie(self) -> str:
        if not self._cookie_value:
            self._download_cookie()
        return self._cookie_value

    # TODO: Validate
    def _download_cookie(self) -> None:
        """Download a session cookie from hulu.com."""
        logger.debug("Downloading cookie:")
        start = monotonic()
        response = self.get_around_client.get(f"{WEB_ORIGIN}/", follow_redirects=True)

        cookies: dict[str, str] = {}
        for redirect_or_response in [*response.history, response]:
            for set_cookie in redirect_or_response.headers.get_list("set-cookie"):
                name, separator, remainder = set_cookie.partition("=")
                if separator:
                    cookies[name.strip()] = remainder.split(";", 1)[0].strip()
        if not cookies:
            msg = f"No session cookie returned by {WEB_ORIGIN}/"
            raise CookieError(msg)

        logger.debug("Downloaded cookie (%.4f s)", monotonic() - start)
        self._cookie_value = "; ".join(
            f"{name}={value}" for name, value in cookies.items()
        )

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: Params,
        headers: dict[str, str],
        log_id: str,
    ) -> str:
        """Download from the API."""
        request_headers = {
            # "Host": Set by httpx
            # "User-Agent":  Set by httpx
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            # "Accept-Encoding": Set by httpx
            "Origin": WEB_ORIGIN,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            # "Connection": Set by httpx
            "Cookie": self._cookie,
            "Priority": "u=4",
            **headers,
        }

        logger.debug("Downloading: %s", log_id)
        url = f"https://{API_DOMAIN}/{endpoint}"
        start = monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers=request_headers,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise ResourceNotFoundError(response.status_code, response.text)
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)
        sleep(self.sleep_time)
        return response.text

    # TODO: Validate
    def download_page(self, path: str, log_id: str) -> str:
        """Download one page of the website."""
        request_headers = {
            # "Host": Set by httpx
            # "User-Agent":  Set by httpx
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            # "Accept-Encoding": Set by httpx
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            # "Connection": Set by httpx
            "Priority": "u=0, i",
        }

        logger.debug("Downloading: %s", log_id)
        start = monotonic()
        response = self.get_around_client.get(
            f"{WEB_ORIGIN}/{path}",
            headers=request_headers,
            follow_redirects=True,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise ResourceNotFoundError(response.status_code, response.text)
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)
        sleep(self.sleep_time)
        return response.text
