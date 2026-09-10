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
from wholoo.search import extract_search


class SearchId(RecordingId[Wholoo]):
    query: str
    name: str

    # TODO: Validate
    def recording_name(self) -> str:
        return self.name

    def download(self, client: Wholoo) -> str:
        return client.search.download(self.query)


def generate_search(client: Wholoo) -> None:
    model_name = "SearchModel"
    queries = load_ids(GENERATOR_PATHS, model_name, SearchId)
    download_missing(GENERATOR_PATHS, model_name, queries, client)
    rebuild_model(GENERATOR_PATHS, model_name, SearchId, extract_search)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(Wholoo(build_client_automatically()))
