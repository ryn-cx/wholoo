# TODO: Validate
"""Exceptions."""

from __future__ import annotations


class WholooError(Exception):
    """Base exception for the wholoo library."""


class HTTPError(WholooError):
    """Raised when an HTTP request fails with an unexpected status code."""
