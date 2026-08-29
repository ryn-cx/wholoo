from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class MetricsInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | None = None
    target_type: str | None = None
    target_name: str | None = None
    selection_tracking_id: UUID | None = None

class Personalization(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bowie_context: str | None = None
    eab: str | None = None

class Accent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hue: int | None = None
    classification: str | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class Horizontal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image | None = None
    text: str | None = None

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    horizontal: Horizontal | None = None

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    index: list[list[int]] | None = None

class Body(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    index: list[list[int]] | None = None

class ShortSubtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    index: list[Any] | None = None

class BrandWatermarkBottomRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogoBottomRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark_bottom_right: BrandWatermarkBottomRight | None = Field(None, alias='brand.watermark.bottom.right')
    brand_logo_bottom_right: BrandLogoBottomRight | None = Field(None, alias='brand.logo.bottom.right')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None
    artwork: Artwork1 | None = None

class Visuals(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    artwork: Artwork | None = None
    headline: Headline | None = None
    body: Body | None = None
    action_text: str | None = None
    short_subtitle: ShortSubtitle | None = None
    primary_branding: PrimaryBranding | None = None

class MetricsInfo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = None
    target_id: UUID | None = None
    target_type: str | None = None
    target_display_name: str | None = None

class Browse(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: UUID | None = None
    target_name: str | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    href: str | None = None
    browse_theme: str | None = None
    metrics_info: MetricsInfo1 | None = None
    type: str | None = None

class MetricsInfo2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | None = None
    target_type: str | None = None
    target_display_name: str | None = None
    eab: str | None = None
    field_type: str | None = Field(None, alias='_type')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = None
    entity_name: str | None = None
    entity_type: str | None = None
    metrics_info: MetricsInfo2 | None = None
    eab: str | None = None

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class Horizontal1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image1 | None = None
    text: str | None = None

class Vertical(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    text: str | None = None

class Artwork2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    horizontal: Horizontal1 | None = None
    vertical: Vertical | None = None

class Browse1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: UUID | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    type: str | None = None

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = None
    entity_name: str | None = None
    entity_type: str | None = None
    metrics_info: MetricsInfo2 | None = None
    browse: Browse1 | None = None
    target_name: str | None = None
    href: str | None = None

class BrandWatermarkBottomRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogoBottomRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 | None = Field(None, alias='brand.watermark.bottom.right')
    brand_logo_bottom_right: BrandLogoBottomRight1 | None = Field(None, alias='brand.logo.bottom.right')

class PrimaryBranding1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None
    artwork: Artwork3 | None = None

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    artwork: Artwork2 | None = None
    action: Action1 | None = None
    primary_branding: PrimaryBranding1 | None = None

class ContextMenu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action] | None = None
    header: Header | None = None

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    start_date: AwareDatetime | None = None
    end_date: AwareDatetime | None = None
    location_requirement: str | None = None
    is_available: bool | None = None

class Rights(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    startover: bool | None = None
    recordable: bool | None = None
    offline: bool | None = None
    client_override: bool | None = None
    co_viewing: bool | None = None

class Bundle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: int | None = None
    eab_id: str | None = None
    network_id: UUID | None = None
    network_name: str | None = None
    duration: int | None = None
    availability: Availability | None = None
    bundle_type: str | None = None
    rating: str | None = None
    open_credit_end_pos: int | None = None
    close_credit_start_pos: int | None = None
    rights: Rights | None = None
    cp_id: int | None = None
    all_etag: str | None = None
    rights_etag: str | None = None
    airings_etag: str | None = None
    stream_etag: str | None = None
    rights_ttl: int | None = None
    airings_ttl: int | None = None
    stream_ttl: int | None = None
    package_id: int | None = None
    av_features: list[Any] | None = None

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | None = None
    target_type: str | None = None
    target_display_name: str | None = None
    eab: str | None = None
    airing_type: str | None = None

class Playback(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eab: str | None = None
    bundle: Bundle | None = None
    metrics_info: MetricsInfo4 | None = None
    type: str | None = None

class Actions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse: Browse | None = None
    context_menu: ContextMenu | None = None
    playback: Playback | None = None

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None

class EntityMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genre_names: list[str] | None = None
    premiere_date: AwareDatetime | None = None
    rating: Rating | None = None
    target_name: str | None = None
    is_warm: bool | None = None
    network_name: str | None = None
    availability: Availability | None = None

class Result(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    metrics_info: MetricsInfo | None = None
    personalization: Personalization | None = None
    device_context_failure: bool | None = None
    view_template: str | None = None
    visuals: Visuals | None = None
    actions: Actions | None = None
    entity_metadata: EntityMetadata | None = None

class Group(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    category: str | None = None
    results: list[Result] | None = None

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    search_result_type: str | None = None
    explanation: str | None = None
    selection_tracking_id: UUID | None = None

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    groups: list[Group] | None = None
    metadata: Metadata | None = None
    device_context_failure: bool | None = None
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
