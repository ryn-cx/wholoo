# TODO: Validate
"""Rebuilds GenresModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing, rebuild_model
from wholoo import Wholoo

NAME = "genres"
"""The genre list is one page, so its recording is filed under one name."""


# TODO: Validate
def generate_genres(client: Wholoo) -> None:
    """Rebuild GenresModel."""
    download_if_missing(FILES_PATH, "GenresModel", NAME, client.genres.download)
    rebuild_model(FILES_PATH, WHOLOO_PATH, "GenresModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_genres(Wholoo(build_client_automatically()))
