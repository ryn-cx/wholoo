"""Contains the Wholoo class."""

from __future__ import annotations

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from get_around import GetAround

from wholoo.exceptions import CookieError, HTTPError
from wholoo.movies import Movies
from wholoo.search import Search
from wholoo.tv import TV

if TYPE_CHECKING:
    from httpx._types import QueryParamTypes

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Wholoo:
    """Hulu API wrapper."""

    def __init__(self, get_around_client: GetAround | None = None) -> None:
        """Initialize the Wholoo client."""
        self.get_around_client = get_around_client or GetAround()
        self.cookie: str = ""

        self.tv = TV(self)
        self.movies = Movies(self)
        self.search = Search(self)

    def _headers(self, referer: str) -> dict[str, str]:
        return {
            # "Host": Set by httpx
            # "User-Agent":  Set by httpx
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            # "Accept-Encoding": Set by httpx
            "Referer": referer,
            "Origin": "https://www.hulu.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            # "Connection": Set by httpx
            "Cookie": self._fetch_cookie(),
            "Priority": "u=4",
        }

    def _fetch_cookie(self) -> str:
        if self.cookie:
            return self.cookie

        response = self.get_around_client.get("https://www.hulu.com/")
        cookies: dict[str, str] = {}
        for set_cookie in response.headers.get_list("set-cookie"):
            name, separator, remainder = set_cookie.partition("=")
            if separator:
                cookies[name.strip()] = remainder.split(";", 1)[0].strip()
        if not cookies:
            msg = "No session cookie returned by https://www.hulu.com/"
            raise CookieError(msg)
        self.cookie = "; ".join(f"{name}={value}" for name, value in cookies.items())
        return self.cookie

    def download(
        self,
        url: str,
        referer: str,
        *,
        params: QueryParamTypes,
        log_id: str,
    ) -> dict[str, Any]:
        """Download a URL and return its JSON response."""
        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers=self._headers(referer),
        )
        if response.is_error:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        parsed: dict[str, Any] = response.json()
        return parsed
