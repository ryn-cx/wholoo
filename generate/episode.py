# TODO: Validate
"""Rebuilds EpisodeModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from wholoo import Wholoo

EPISODE_IDS = load_ids("EpisodeModel")


# TODO: Validate
def generate_episode(client: Wholoo) -> None:
    """Rebuild EpisodeModel."""
    for episode_id in EPISODE_IDS:
        download_if_missing(
            FILES_PATH,
            "EpisodeModel",
            episode_id,
            lambda episode_id=episode_id: client.episode.download(episode_id),
        )
    rebuild_model(FILES_PATH, WHOLOO_PATH, "EpisodeModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_episode(Wholoo(build_client_automatically()))
