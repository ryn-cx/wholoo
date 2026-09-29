# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import GenreModel as OptionalModel
from .strict_models import GenreModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        GenreModel,
        Item,
    )
else:
    from .optional_models import (
        GenreModel,
        Item,
    )

__all__ = [
    "GenreModel",
    "Item",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> GenreModel:
    """Read a downloaded file into GenreModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
