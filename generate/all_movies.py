# TODO: Validate
"""Rebuilds AllMoviesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing, rebuild_model
from wholoo import Wholoo

NAME = "movies"
"""The movie list is one page, so its recording is filed under one name."""


# TODO: Validate
def generate_all_movies(client: Wholoo) -> None:
    """Rebuild AllMoviesModel."""
    download_if_missing(FILES_PATH, "AllMoviesModel", NAME, client.all_movies.download)
    rebuild_model(FILES_PATH, WHOLOO_PATH, "AllMoviesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_all_movies(Wholoo(build_client_automatically()))
