from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from typing import Any

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    href: str

class GenreModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    title: str
    view_all_url: None = Field(..., alias='viewAllUrl')
    items: list[Item]
    url_format: None = Field(..., alias='urlFormat')
    metrics: dict[str, Any]
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
