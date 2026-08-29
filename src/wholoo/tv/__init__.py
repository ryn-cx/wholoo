# TODO: Validate
"""Contains the TV class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import ClassVar

from wholoo.discover_hub import DiscoverHub
from wholoo.exceptions import ResourceNotFoundError, SeriesNotFoundError
from wholoo.tv.models import TVModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TV(DiscoverHub):
    """Manage the series details file.

    The page lists the series' seasons but not their episodes, which come from
    the season endpoint.

    Source: https://www.hulu.com/series/{content_id}
    """

    content_type: ClassVar[str] = "series"

    # TODO: Validate
    def __call__(self, content_id: str, *, cache_key: str | None = None) -> TVModel:
        """Look the series up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(content_id, cache_key=cache_key), log_id)

    # TODO: Validate
    def download(self, content_id: str, *, cache_key: str | None = None) -> str:
        """Download the series details file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(content_id, cache_key, log_id)
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(
                content_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TVModel:
        """Read a downloaded series details file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
