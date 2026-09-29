# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import AllMoviesModel as OptionalModel
from .strict_models import AllMoviesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        AllMoviesModel,
        Item,
    )
else:
    from .optional_models import (
        AllMoviesModel,
        Item,
    )

__all__ = [
    "AllMoviesModel",
    "Item",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> AllMoviesModel:
    """Read a downloaded file into AllMoviesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
