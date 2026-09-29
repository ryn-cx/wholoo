from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class GenreModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    view_all_url: Any | None = Field(None, alias='viewAllUrl')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    url_format: Any | None = Field(None, alias='urlFormat')
    metrics: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
