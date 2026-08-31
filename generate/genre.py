# TODO: Validate
"""Rebuilds GenreModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from wholoo import Wholoo

GENRE_IDS = load_ids("GenreModel")


# TODO: Validate
def generate_genre(client: Wholoo) -> None:
    """Rebuild GenreModel."""
    for genre_id in GENRE_IDS:
        download_if_missing(
            FILES_PATH,
            "GenreModel",
            genre_id,
            lambda genre_id=genre_id: client.genre.download(genre_id),
        )
    rebuild_model(FILES_PATH, WHOLOO_PATH, "GenreModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_genre(Wholoo(build_client_automatically()))
