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
from wholoo.episode import extract_episode


class EpisodeId(RecordingId[Wholoo]):
    episode_id: str

    def download(self, client: Wholoo) -> str:
        return client.episode.download(self.episode_id)


def generate_episode(client: Wholoo) -> None:
    model_name = "EpisodeModel"
    episode_ids = load_ids(GENERATOR_PATHS, model_name, EpisodeId)
    download_missing(GENERATOR_PATHS, model_name, episode_ids, client)
    rebuild_model(GENERATOR_PATHS, model_name, EpisodeId, extract_episode)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_episode(Wholoo(build_client_automatically()))
