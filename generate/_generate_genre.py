from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from wholoo import Wholoo
from wholoo.sitemap_page import extract_list_card


class GenreId(RecordingId[Wholoo]):
    genre_id: str

    def download(self, client: Wholoo) -> str:
        return client.genre.download(self.genre_id)


def generate_genre(client: Wholoo) -> None:
    model_name = "GenreModel"
    genre_ids = load_ids(GENERATOR_PATHS, model_name, GenreId)
    download_missing(GENERATOR_PATHS, model_name, genre_ids, client)
    rebuild_model(GENERATOR_PATHS, model_name, GenreId, extract_list_card)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_genre(Wholoo(build_client_automatically()))
