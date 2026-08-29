# TODO: Validate
"""Contains the Movies class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import ClassVar

from wholoo.discover_hub import DiscoverHub
from wholoo.exceptions import MovieNotFoundError, ResourceNotFoundError
from wholoo.movies.models import MoviesModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Movies(DiscoverHub):
    """Manage the movie details file.

    Source: https://www.hulu.com/movie/{content_id}
    """

    content_type: ClassVar[str] = "movie"

    # TODO: Validate
    def __call__(self, content_id: str, *, cache_key: str | None = None) -> MoviesModel:
        """Look the movie up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(content_id, cache_key=cache_key), log_id)

    # TODO: Validate
    def download(self, content_id: str, *, cache_key: str | None = None) -> str:
        """Download the movie details file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._download(content_id, cache_key, log_id)
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(
                content_id,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, content_id)

    # TODO: Validate
    def _validate_download(self, response: str, content_id: str) -> str:
        """Check that the hub describes a movie.

        An id nothing is under is answered with a 200 carrying a hub that has
        no entity in it.
        """
        if not json.loads(response).get("details", {}).get("entity"):
            raise MovieNotFoundError(content_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MoviesModel:
        """Read a downloaded movie details file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
