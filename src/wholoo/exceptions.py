# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class WholooError(Exception):
    """Base exception for Wholoo."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(WholooError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


# TODO: Validate
class MovieNotFoundError(ResourceNotFoundError):
    """Raised when the requested movie does not exist."""

    # TODO: Validate
    def __init__(
        self,
        content_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the movie id and the originating response."""
        self.content_id = content_id
        super().__init__(status_code, response)


# TODO: Validate
class SeriesNotFoundError(ResourceNotFoundError):
    """Raised when the requested series does not exist."""

    # TODO: Validate
    def __init__(
        self,
        content_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the series id and the originating response."""
        self.content_id = content_id
        super().__init__(status_code, response)


# TODO: Validate
class SeasonNotFoundError(ResourceNotFoundError):
    """Raised when the requested season of a series does not exist."""

    # TODO: Validate
    def __init__(
        self,
        series_id: str,
        season: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the series id, season number and originating response."""
        self.series_id = series_id
        self.season = season
        super().__init__(status_code, response)


# TODO: Validate
class CookieError(WholooError):
    """Raised when hulu.com answers without setting a session cookie."""
