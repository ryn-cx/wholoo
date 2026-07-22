# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Mapping


class WholooError(Exception):
    """Base exception for the wholoo library."""


class HTTPError(WholooError):
    """Raised when an HTTP request fails with an unexpected status code."""


class CookieError(WholooError):
    """Raised when no session cookie could be obtained."""


class InvalidSeasonError(WholooError):
    """Raised when a requested season number returns no episodes.

    The offending :attr:`response` is retained for inspection.
    """

    def __init__(self, response: Mapping[str, Any]) -> None:
        """Store the response and set the message."""
        self.response = response
        super().__init__("Invalid season number")
