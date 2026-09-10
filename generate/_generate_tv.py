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


class TVId(RecordingId[Wholoo]):
    content_id: str

    def download(self, client: Wholoo) -> str:
        return client.tv.download(self.content_id)


def generate_tv(client: Wholoo) -> None:
    model_name = "TVModel"
    content_ids = load_ids(GENERATOR_PATHS, model_name, TVId)
    download_missing(GENERATOR_PATHS, model_name, content_ids, client)
    rebuild_model(GENERATOR_PATHS, model_name, TVId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv(Wholoo(build_client_automatically()))
