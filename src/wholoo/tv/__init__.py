# TODO: Validate
"""Contains the TV class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, ClassVar

from wholoo.discover_hub import DiscoverHubEndpoint
from wholoo.season import Season
from wholoo.tv.models import TVModel

if TYPE_CHECKING:
    from wholoo import Wholoo

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TV(DiscoverHubEndpoint[TVModel]):
    """Manage the TV file.

    Wraps the ``GET https://discover.hulu.com/content/v5/hubs/series/<id>`` request
    that populates a series' details page. Per-season episode collections are
    available via :attr:`season`.
    """

    _content_type: ClassVar[str] = "series"
    _response_model = TVModel

    def __init__(self, client: Wholoo) -> None:
        """Initialize the series endpoint and its ``season`` sub-endpoint."""
        super().__init__(client)
        self.season = Season(client)
