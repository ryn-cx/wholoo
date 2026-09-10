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
from wholoo.movies import extract_movie


class MoviesId(RecordingId[Wholoo]):
    content_id: str

    def download(self, client: Wholoo) -> str:
        return client.movies.download(self.content_id)


def generate_movies(client: Wholoo) -> None:
    model_name = "MoviesModel"
    content_ids = load_ids(GENERATOR_PATHS, model_name, MoviesId)
    download_missing(GENERATOR_PATHS, model_name, content_ids, client)
    rebuild_model(GENERATOR_PATHS, model_name, MoviesId, extract_movie)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movies(Wholoo(build_client_automatically()))
