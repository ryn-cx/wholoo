# TODO: Validate
"""Contains the Movies class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import ClassVar

from wholoo.discover_hub import DiscoverHubEndpoint
from wholoo.movies.models import MoviesModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Movies(DiscoverHubEndpoint[MoviesModel]):
    """Manage the movies file.

    Wraps the ``GET https://discover.hulu.com/content/v5/hubs/movie/<id>`` request
    that populates a movie's details page.
    """

    _content_type: ClassVar[str] = "movie"
    _response_model = MoviesModel
