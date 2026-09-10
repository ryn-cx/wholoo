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


class AllMoviesId(RecordingId[Wholoo]):
    page: str

    def download(self, client: Wholoo) -> str:
        return client.all_movies.download()


def generate_all_movies(client: Wholoo) -> None:
    model_name = "AllMoviesModel"
    pages = load_ids(GENERATOR_PATHS, model_name, AllMoviesId)
    download_missing(GENERATOR_PATHS, model_name, pages, client)
    rebuild_model(GENERATOR_PATHS, model_name, AllMoviesId, extract_list_card)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_all_movies(Wholoo(build_client_automatically()))
