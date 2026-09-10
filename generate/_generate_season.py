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


class SeasonId(RecordingId[Wholoo]):
    series_id: str
    season: int
    name: str

    def recording_name(self) -> str:
        return self.name

    def download(self, client: Wholoo) -> str:
        return client.season.download(self.series_id, self.season)


def generate_season(client: Wholoo) -> None:
    model_name = "SeasonModel"
    seasons = load_ids(GENERATOR_PATHS, model_name, SeasonId)
    download_missing(GENERATOR_PATHS, model_name, seasons, client)
    rebuild_model(GENERATOR_PATHS, model_name, SeasonId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season(Wholoo(build_client_automatically()))
