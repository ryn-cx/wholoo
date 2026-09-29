from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class MetricsInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | str | Any = Field(default=None, union_mode='left_to_right')
    target_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_name: str | Any = Field(default=None, union_mode='left_to_right')
    selection_tracking_id: UUID | Any = Field(default=None, union_mode='left_to_right')

class Personalization(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bowie_context: str | Any = Field(default=None, union_mode='left_to_right')
    eab: str | Any = Field(default=None, union_mode='left_to_right')

class Accent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hue: int | Any = Field(default=None, union_mode='left_to_right')
    classification: str | Any = Field(default=None, union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Horizontal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    artwork_type: str | Any = Field(default=None, union_mode='left_to_right')
    image: Image | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    horizontal: Horizontal | Any = Field(default=None, union_mode='left_to_right')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    index: list[list[int]] | Any = Field(default=None, union_mode='left_to_right')

class Body(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    index: list[list[int]] | Any = Field(default=None, union_mode='left_to_right')

class ShortSubtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    index: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkBottomRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoBottomRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark_bottom_right: BrandWatermarkBottomRight | Any = Field(None, alias='brand.watermark.bottom.right', union_mode='left_to_right')
    brand_logo_bottom_right: BrandLogoBottomRight | Any = Field(None, alias='brand.logo.bottom.right', union_mode='left_to_right')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork1 | Any = Field(default=None, union_mode='left_to_right')

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    index: list[list[int]] | Any = Field(default=None, union_mode='left_to_right')

class ShortBody(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    index: list[list[int]] | Any = Field(default=None, union_mode='left_to_right')

class Visuals(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    artwork: Artwork | Any = Field(default=None, union_mode='left_to_right')
    headline: Headline | Any = Field(default=None, union_mode='left_to_right')
    body: Body | Any = Field(default=None, union_mode='left_to_right')
    action_text: str | Any = Field(default=None, union_mode='left_to_right')
    short_subtitle: ShortSubtitle | Any = Field(default=None, union_mode='left_to_right')
    primary_branding: PrimaryBranding | Any = Field(default=None, union_mode='left_to_right')
    subtitle: Subtitle | Any = Field(default=None, union_mode='left_to_right')
    short_body: ShortBody | Any = Field(default=None, union_mode='left_to_right')

class Params(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    network_breadcrumb: UUID | Any = Field(default=None, union_mode='left_to_right')

class MetricsInfo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | str | Any = Field(default=None, union_mode='left_to_right')
    target_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_display_name: str | Any = Field(default=None, union_mode='left_to_right')

class Browse(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | str | Any = Field(default=None, union_mode='left_to_right')
    target_name: str | Any = Field(default=None, union_mode='left_to_right')
    target_theme: str | Any = Field(default=None, union_mode='left_to_right')
    params: Params | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    browse_theme: str | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo1 | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class MetricsInfo2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    target_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_display_name: str | Any = Field(default=None, union_mode='left_to_right')
    eab: str | Any = Field(default=None, union_mode='left_to_right')
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | Any = Field(default=None, union_mode='left_to_right')
    entity_name: str | Any = Field(default=None, union_mode='left_to_right')
    entity_type: str | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo2 | Any = Field(default=None, union_mode='left_to_right')
    eab: str | Any = Field(default=None, union_mode='left_to_right')

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Horizontal1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    artwork_type: str | Any = Field(default=None, union_mode='left_to_right')
    image: Image1 | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Vertical(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    artwork_type: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    horizontal: Horizontal1 | Any = Field(default=None, union_mode='left_to_right')
    vertical: Vertical | Any = Field(default=None, union_mode='left_to_right')

class Browse1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    target_theme: str | Any = Field(default=None, union_mode='left_to_right')
    params: Params | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | Any = Field(default=None, union_mode='left_to_right')
    entity_name: str | Any = Field(default=None, union_mode='left_to_right')
    entity_type: str | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo2 | Any = Field(default=None, union_mode='left_to_right')
    browse: Browse1 | Any = Field(default=None, union_mode='left_to_right')
    target_name: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkBottomRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoBottomRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 | Any = Field(None, alias='brand.watermark.bottom.right', union_mode='left_to_right')
    brand_logo_bottom_right: BrandLogoBottomRight1 | Any = Field(None, alias='brand.logo.bottom.right', union_mode='left_to_right')

class PrimaryBranding1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork3 | Any = Field(default=None, union_mode='left_to_right')

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork2 | Any = Field(default=None, union_mode='left_to_right')
    action: Action1 | Any = Field(default=None, union_mode='left_to_right')
    primary_branding: PrimaryBranding1 | Any = Field(default=None, union_mode='left_to_right')

class ContextMenu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action] | Any = Field(default=None, union_mode='left_to_right')
    header: Header | Any = Field(default=None, union_mode='left_to_right')

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    start_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    end_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    location_requirement: str | Any = Field(default=None, union_mode='left_to_right')
    is_available: bool | Any = Field(default=None, union_mode='left_to_right')

class Rights(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    startover: bool | Any = Field(default=None, union_mode='left_to_right')
    recordable: bool | Any = Field(default=None, union_mode='left_to_right')
    offline: bool | Any = Field(default=None, union_mode='left_to_right')
    client_override: bool | Any = Field(default=None, union_mode='left_to_right')
    co_viewing: bool | Any = Field(default=None, union_mode='left_to_right')

class Bundle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    eab_id: str | Any = Field(default=None, union_mode='left_to_right')
    network_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    network_name: str | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    availability: Availability | Any = Field(default=None, union_mode='left_to_right')
    bundle_type: str | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    open_credit_end_pos: int | Any = Field(default=None, union_mode='left_to_right')
    close_credit_start_pos: int | Any = Field(default=None, union_mode='left_to_right')
    rights: Rights | Any = Field(default=None, union_mode='left_to_right')
    cp_id: int | Any = Field(default=None, union_mode='left_to_right')
    all_etag: str | Any = Field(default=None, union_mode='left_to_right')
    rights_etag: str | Any = Field(default=None, union_mode='left_to_right')
    airings_etag: str | Any = Field(default=None, union_mode='left_to_right')
    stream_etag: str | Any = Field(default=None, union_mode='left_to_right')
    rights_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    airings_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    stream_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(default=None, union_mode='left_to_right')
    av_features: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    target_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_display_name: str | Any = Field(default=None, union_mode='left_to_right')
    eab: str | Any = Field(default=None, union_mode='left_to_right')
    airing_type: str | Any = Field(default=None, union_mode='left_to_right')

class Playback(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eab: str | Any = Field(default=None, union_mode='left_to_right')
    bundle: Bundle | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo4 | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class GetRelated(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entity_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    entity_type: str | Any = Field(default=None, union_mode='left_to_right')
    view_template: str | Any = Field(default=None, union_mode='left_to_right')

class Actions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse: Browse | Any = Field(default=None, union_mode='left_to_right')
    context_menu: ContextMenu | Any = Field(default=None, union_mode='left_to_right')
    playback: Playback | Any = Field(default=None, union_mode='left_to_right')
    get_related: GetRelated | Any = Field(default=None, union_mode='left_to_right')

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | Any = Field(default=None, union_mode='left_to_right')

class Availability1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    start_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    end_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    location_requirement: str | Any = Field(default=None, union_mode='left_to_right')
    is_available: bool | Any = Field(default=None, union_mode='left_to_right')
    stormflow_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    airing_start_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    airing_end_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')

class EntityMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genre_names: list[str] | Any = Field(default=None, union_mode='left_to_right')
    premiere_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    rating: Rating | Any = Field(default=None, union_mode='left_to_right')
    target_name: str | Any = Field(default=None, union_mode='left_to_right')
    is_warm: bool | Any = Field(default=None, union_mode='left_to_right')
    network_name: str | Any = Field(default=None, union_mode='left_to_right')
    availability: Availability1 | Any = Field(default=None, union_mode='left_to_right')
    league_name: str | Any = Field(default=None, union_mode='left_to_right')
    sport_name: str | Any = Field(default=None, union_mode='left_to_right')

class Result(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    metrics_info: MetricsInfo | Any = Field(default=None, union_mode='left_to_right')
    personalization: Personalization | Any = Field(default=None, union_mode='left_to_right')
    device_context_failure: bool | Any = Field(default=None, union_mode='left_to_right')
    view_template: str | Any = Field(default=None, union_mode='left_to_right')
    visuals: Visuals | Any = Field(default=None, union_mode='left_to_right')
    actions: Actions | Any = Field(default=None, union_mode='left_to_right')
    entity_metadata: EntityMetadata | Any = Field(default=None, union_mode='left_to_right')

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    category: str | Any = Field(default=None, union_mode='left_to_right')
    results: list[Result] | Any = Field(default=None, union_mode='left_to_right')
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
