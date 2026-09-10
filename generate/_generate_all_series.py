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


class AllSeriesId(RecordingId[Wholoo]):
    page: str

    def download(self, client: Wholoo) -> str:
        return client.all_series.download()


def generate_all_series(client: Wholoo) -> None:
    model_name = "AllSeriesModel"
    pages = load_ids(GENERATOR_PATHS, model_name, AllSeriesId)
    download_missing(GENERATOR_PATHS, model_name, pages, client)
    rebuild_model(GENERATOR_PATHS, model_name, AllSeriesId, extract_list_card)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_all_series(Wholoo(build_client_automatically()))
