# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from wholoo.episode.models import EpisodeModel
from wholoo.exceptions import EpisodeNotFoundError, HTTPError

if TYPE_CHECKING:
    from wholoo import Wholoo

EPISODE_IDS = [
    # https://www.hulu.com/watch/570d3e7f-ba64-48e8-8f8a-5ff0480798fe
    pytest.param("570d3e7f-ba64-48e8-8f8a-5ff0480798fe", id="the belchies"),
    # https://www.hulu.com/watch/0902273c-4977-4431-8f70-6468fc9fed22
    pytest.param("0902273c-4977-4431-8f70-6468fc9fed22", id="monsieur grenouille"),
]

SERIES_IDS = {
    "570d3e7f-ba64-48e8-8f8a-5ff0480798fe": "fdeb1018-4472-442f-ba94-fb087cdea069",
    "0902273c-4977-4431-8f70-6468fc9fed22": "77db3944-8426-4259-94c8-be147d3e7594",
}
"""The series each episode belongs to, which is what the hub is looked up for."""


# TODO: Validate
class EpisodeTest(RecordedEndpoint):
    MODEL = EpisodeModel


# TODO: Validate
@pytest.mark.parametrize("episode_id", EPISODE_IDS)
def test_download(client: Wholoo, episode_id: str) -> None:
    EpisodeTest.download_test(episode_id, lambda: client.episode.download(episode_id))


# TODO: Validate
@pytest.mark.parametrize("episode_id", EPISODE_IDS)
def test_parse(client: Wholoo, episode_id: str) -> None:
    episode = client.episode.load(EpisodeTest.recorded_content(episode_id))
    assert str(episode.id) == episode_id
    assert str(episode.details.entity.series_id) == SERIES_IDS[episode_id]


# TODO: Validate
@pytest.mark.parametrize(
    "episode_id",
    [
        pytest.param(
            "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            id="episode that does not exist",
        ),
    ],
)
def test_download_invalid(client: Wholoo, episode_id: str) -> None:
    EpisodeTest.error_test(
        episode_id,
        lambda: client.episode.download(episode_id),
        EpisodeNotFoundError,
    )


# TODO: Validate
@pytest.mark.parametrize(
    "episode_id",
    [pytest.param("AAAAAAAA", id="id that is not shaped like one")],
)
def test_download_malformed(client: Wholoo, episode_id: str) -> None:
    EpisodeTest.error_test(
        episode_id,
        lambda: client.episode.download(episode_id),
        HTTPError,
    )
