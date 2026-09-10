# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from wholoo.exceptions import EpisodeNotFoundError, HTTPError

if TYPE_CHECKING:
    from wholoo import Wholoo

EPISODE_IDS = [
    pytest.param("570d3e7f-ba64-48e8-8f8a-5ff0480798fe", id="the belchies"),
    pytest.param("0902273c-4977-4431-8f70-6468fc9fed22", id="monsieur grenouille"),
]


# TODO: Validate
@pytest.mark.parametrize("episode_id", EPISODE_IDS)
def test_download(client: Wholoo, episode_id: str) -> None:
    episode = client.episode(episode_id)
    assert str(episode.entity.id) == episode_id
    assert episode.entity.series_id


# TODO: Validate
def test_download_invalid(client: Wholoo) -> None:
    # This tests the raise in _validate_download which is triggered by an
    # invalid episode_id.
    with pytest.raises(EpisodeNotFoundError):
        client.episode.download("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")


# TODO: Validate
def test_download_malformed(client: Wholoo) -> None:
    # This tests the raise in download which is triggered by a malformed
    # episode_id.
    with pytest.raises(EpisodeNotFoundError):
        client.episode.download("")


# TODO: Validate
def test_download_http_error(client: Wholoo) -> None:
    with pytest.raises(HTTPError):
        client.episode.download("AAAAAAAA")
