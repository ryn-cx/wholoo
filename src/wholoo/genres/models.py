# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import GenresModel as OptionalModel
from .strict_models import GenresModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        GenresModel,
        Item,
    )
else:
    from .optional_models import (
        GenresModel,
        Item,
    )

__all__ = [
    "GenresModel",
    "Item",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> GenresModel:
    """Read a downloaded file into GenresModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
