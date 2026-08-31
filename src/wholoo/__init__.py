# TODO: Validate
"""Contains the Wholoo class."""

from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from time import monotonic, sleep
from typing import TYPE_CHECKING

from get_around import GetAround

from wholoo.collection import Collection
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


# TODO: Validate
class Wholoo:
    """Hulu API wrapper."""

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        sleep_time: float = 0,
    ) -> None:
        """Initializes the Wholoo client.

        The client holds one attribute per endpoint, so `client.movies(id)`
        looks a movie up and `client.movies.download(id)` and
        `client.movies.load(data)` are the halves of it.
        """
        self.get_around_client = get_around_client or GetAround()
        self.sleep_time = sleep_time
        self._cookie_value = ""

        self.movies = Movies(self)
        self.tv = TV(self)
        self.season = Season(self)
        self.episode = Episode(self)
        self.collection = Collection(self)
        self.search = Search(self)
        self.genres = Genres(self)
        self.genre = Genre(self)

    # TODO: Validate
    @property
    def _cookie(self) -> str:
        if not self._cookie_value:
            self._download_cookie()
        return self._cookie_value

    # TODO: Validate
    def _download_cookie(self) -> None:
        """Ask hulu.com for a session cookie.

        Raises:
            CookieError: If the site answers without setting any cookie.
        """
        logger.debug("Downloading cookie:")
        start = monotonic()
        response = self.get_around_client.get(f"{WEB_ORIGIN}/")

        cookies: dict[str, str] = {}
        for set_cookie in response.headers.get_list("set-cookie"):
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
        """Downloads from the API.

        What comes back is the body as it was served, and reading it into a
        model is the endpoint's `load`.

        Raises:
            ResourceNotFoundError: If the API says the thing does not exist.
            HTTPError: If the request is answered with any other error.
        """
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
        """Downloads one page of the website.

        What comes back is the HTML as it was served, and picking the data
        out of it is the endpoint's own.

        Raises:
            ResourceNotFoundError: If the site says the page does not exist.
            HTTPError: If the request is answered with any other error.
        """
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
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise ResourceNotFoundError(response.status_code, response.text)
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)
        sleep(self.sleep_time)
        return response.text
