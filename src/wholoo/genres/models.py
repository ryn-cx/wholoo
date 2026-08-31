"""GenresModel, strict to a type checker, all-optional at runtime.

A type checker reads the strict model, so every field carries the type and
the requiredness the schema recorded. At runtime the all-optional copy is imported
instead, so a response that has drifted still parses and a field the data is
missing is None despite what its type hint says.
"""

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import GenresModel as OptionalModel
from .strict_models import GenresModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        BigFooterItem,
        CartAbandonmentCopy,
        Component,
        Config,
        ContentOverrides,
        DatadogRum,
        Endpoints,
        FeatureFlags,
        GenresModel,
        Geodata,
        HasBotifyPageWorkerEnabled,
        Item,
        Item1,
        Keys,
        Layout,
        Metatag,
        Metrics,
        Modal,
        OneTrust,
        Options,
        PageProps,
        Program,
        Props,
        Query,
        RuntimeConfig,
        Section,
        User,
    )
else:
    from .optional_models import (
        BigFooterItem,
        CartAbandonmentCopy,
        Component,
        Config,
        ContentOverrides,
        DatadogRum,
        Endpoints,
        FeatureFlags,
        GenresModel,
        Geodata,
        HasBotifyPageWorkerEnabled,
        Item,
        Item1,
        Keys,
        Layout,
        Metatag,
        Metrics,
        Modal,
        OneTrust,
        Options,
        PageProps,
        Program,
        Props,
        Query,
        RuntimeConfig,
        Section,
        User,
    )

__all__ = [
    "BigFooterItem",
    "CartAbandonmentCopy",
    "Component",
    "Config",
    "ContentOverrides",
    "DatadogRum",
    "Endpoints",
    "FeatureFlags",
    "GenresModel",
    "Geodata",
    "HasBotifyPageWorkerEnabled",
    "Item",
    "Item1",
    "Keys",
    "Layout",
    "Metatag",
    "Metrics",
    "Modal",
    "OneTrust",
    "Options",
    "PageProps",
    "Program",
    "Props",
    "Query",
    "RuntimeConfig",
    "Section",
    "User",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> GenresModel:
    """Read a downloaded file into GenresModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
