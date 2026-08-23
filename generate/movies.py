# TODO: Validate
"""Rebuilds MoviesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing
from wholoo import Wholoo

CONTENT_IDS = ["4ee4f57e-19bd-493f-96f9-ad3e753af981"]


# TODO: Validate
def generate_movies(client: Wholoo) -> None:
    """Rebuild MoviesModel."""
    for content_id in CONTENT_IDS:
        download_if_missing(
            FILES_PATH,
            "MoviesModel",
            content_id,
            lambda content_id=content_id: client.movies.download(content_id),
        )
    generate_model(FILES_PATH, WHOLOO_PATH, "MoviesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movies(Wholoo(build_client_automatically()))
