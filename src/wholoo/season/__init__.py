# TODO: Validate
"""Contains the Season class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.season.models import SeasonModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())

# The discover collection that lists one season's episodes. Unlike the series
# details hub (``/hubs/series/<id>``, ``_type: hub``), this season sub-hub returns
# a ``_type: collection`` payload whose ``items`` are the season's episodes.
_SEASON_URL = (
    "https://discover.hulu.com/content/v5/hubs/series/{series_id}/season/{season}"
)


class Season(BaseEndpoint[SeasonModel]):
    """Manage the season file.

    Wraps ``GET https://discover.hulu.com/content/v5/hubs/series/<id>/season/<n>``.
    """

    _response_model = SeasonModel

    def get_log_id(self, series_id: str, season: int) -> str:
        """Build the log id for a download."""
        return f"{self.__class__.__name__} {series_id=} {season=}"

    @staticmethod
    def _params(offset: int) -> dict[str, str]:
        return {
            "schema": "3",
            "limit": "1999",
            "offset": str(offset),
            "device_info": "web:4.44.1",
            "referralHost": "production",
        }

    def download(
        self,
        series_id: str,
        season: int,
        *,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Downloads one season's episode collection.

        Args:
            series_id: The Hulu series id, e.g.
                ``"77db3944-8426-4259-94c8-be147d3e7594"``.
            season: The season number to fetch (e.g. ``3``).
            offset: The pagination offset; the default returns the season's first
                (and, at ``limit=1999``, only) page.
        """
        url = _SEASON_URL.format(series_id=series_id, season=season)
        return self._client.download(
            url,
            referer=f"https://www.hulu.com/series/{series_id}",
            params=self._params(offset),
            log_id=self.get_log_id(series_id, season),
        )

    def download_and_parse(self, series_id: str, season: int) -> SeasonModel:
        """Downloads and parses one season's episode collection."""
        return self.parse(self.download(series_id, season))
