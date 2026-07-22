# TODO: Validate
"""Contains the Season class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.exceptions import InvalidSeasonError
from wholoo.season.models import SeasonModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())

# The discover collection that lists one season's episodes. Unlike the series
# details hub (``/hubs/series/<id>``, ``_type: hub``), this season sub-hub returns
# a ``_type: collection`` payload whose ``items`` are the season's episodes.
_SEASON_URL = (
    "https://discover.hulu.com/content/v5/hubs/series/{series_id}/season/{season}"
)


class Season(BaseEndpoint[SeasonModel, [str, int]]):
    """Manage the season file.

    Wraps ``GET https://discover.hulu.com/content/v5/hubs/series/<id>/season/<n>``.
    """

    _response_model = SeasonModel

    @staticmethod
    def _params(offset: int) -> dict[str, str]:
        return {
            "schema": "3",
            "limit": "1999",
            "offset": str(offset),
            "device_info": "web:4.44.1",
            "referralHost": "production",
        }

    @override
    def download(
        self,
        series_id: str,
        season: int,
        *,
        offset: int = 0,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        url = _SEASON_URL.format(series_id=series_id, season=season)
        response = self._client.download(
            url,
            referer=f"https://www.hulu.com/series/{series_id}",
            params=self._params(offset),
            log_id=log_id,
        )
        if not response["pagination"]["total_count"]:
            raise InvalidSeasonError(response)
        return response


    @override
    def download_and_parse(self, series_id: str, season: int) -> SeasonModel:
        return self.parse(self.download(series_id, season))
