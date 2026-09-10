# TODO: Validate
"""Contains the TV class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from wholoo.discover_hub import DiscoverHub
from wholoo.exceptions import ResourceNotFoundError, SeriesNotFoundError
from wholoo.tv.models import TVModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TV(DiscoverHub):
    """Contains information about a specific series.

    The file lists the series' seasons but not their episodes, which come from
    the season endpoint.

    - Example Request:
        - URL: https://www.hulu.com/series/{content_id}
    """

    # TODO: Validate
    def __call__(self, content_id: str) -> TVModel:
        """Download and parse the TV file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(content_id), log_id)

    # TODO: Validate
    def download(self, content_id: str) -> str:
        """Download the TV file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download("series", content_id, 1999, log_id)
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(
                content_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TVModel:
        """Load a TV file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
