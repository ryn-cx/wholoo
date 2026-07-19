# TODO: Validate
"""Contains the Wholoo class."""

from __future__ import annotations

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from wholoo.exceptions import HTTPError
from wholoo.movies import Movies
from wholoo.search import Search
from wholoo.tv import TV

logger = getLogger(__name__)
logger.addHandler(NullHandler())

ORIGIN = "https://www.hulu.com"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0"
)


class Wholoo:
    """Hulu API wrapper."""

    def __init__(self, get_around_client: GetAround | None = None) -> None:
        """Initialize the Wholoo client."""
        self.get_around_client = get_around_client or GetAround()
        self._cookie_header: str | None = None

        self.tv = TV(self)
        self.movies = Movies(self)
        self.search = Search(self)

    def _headers(self, referer: str) -> dict[str, str]:
        """Headers for a same-site REST GET against ``discover.hulu.com``."""
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": ORIGIN,
            "Referer": referer,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Priority": "u=4",
        }
        if self._cookie_header:
            headers["Cookie"] = self._cookie_header
        return headers

    def _bootstrap_session(self, referer: str) -> None:
        """Fetch a Hulu page once to obtain the anonymous session cookies.

        The discover endpoints return a null payload unless the request carries
        the anonymous ``_hulu_at`` token (and companions) that Hulu sets on the
        first page visit. No login is involved.

        The cookies are read straight from the bootstrap response's ``Set-Cookie``
        headers and forwarded as an explicit ``Cookie`` header, rather than relying
        on the HTTP client's cookie jar: when requests are routed through a proxy
        the request host is not ``hulu.com``, so a jar would drop the
        ``Domain=.hulu.com`` cookies.
        """
        if self._cookie_header is not None:
            return
        response = self.get_around_client.get(
            referer,
            headers={
                "User-Agent": USER_AGENT,
                "Accept-Language": "en-US,en;q=0.9",
            },
        )
        cookies: dict[str, str] = {}
        for set_cookie in response.headers.get_list("set-cookie"):
            name, sep, rest = set_cookie.partition("=")
            if sep:
                cookies[name.strip()] = rest.split(";", 1)[0].strip()
        self._cookie_header = "; ".join(
            f"{name}={value}" for name, value in cookies.items()
        )

    def download(
        self,
        url: str,
        referer: str,
        *,
        params: dict[str, str],
        log_id: str,
    ) -> dict[str, Any]:
        """GET a Hulu REST endpoint (``discover.hulu.com``) and return its JSON.

        The anonymous-session cookies picked up by :meth:`_bootstrap_session` are
        set with ``Domain=.hulu.com``, so they are valid for the sibling
        ``discover.hulu.com`` host.
        """
        logger.debug("Downloading: %s", log_id)
        self._bootstrap_session(referer)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers=self._headers(referer),
        )
        if response.status_code != HTTPStatus.OK:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        parsed: dict[str, Any] = response.json()
        return parsed
