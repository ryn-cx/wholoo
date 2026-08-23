from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any

class MetricsInfo(BaseModel):
    target_id: UUID
    target_type: str
    target_name: str
    selection_tracking_id: UUID

class Personalization(BaseModel):
    bowie_context: str
    eab: str

class Accent(BaseModel):
    hue: int
    classification: str

class Image(BaseModel):
    path: str
    accent: Accent
    image_id: str

class Horizontal(BaseModel):
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image
    text: str

class Artwork(BaseModel):
    field_type: str = Field(..., alias='_type')
    horizontal: Horizontal

class Headline(BaseModel):
    text: str
    index: list[list[int]]

class Body(BaseModel):
    text: str
    index: list[list[int]]

class ShortSubtitle(BaseModel):
    text: str
    index: list[None]

class BrandWatermarkBottomRight(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork1(BaseModel):
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_bottom_right: BrandLogoBottomRight = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding(BaseModel):
    id: UUID
    name: str
    artwork: Artwork1

class Visuals(BaseModel):
    artwork: Artwork
    headline: Headline
    body: Body
    action_text: str
    short_subtitle: ShortSubtitle
    primary_branding: PrimaryBranding | None = None

class MetricsInfo1(BaseModel):
    action_type: str
    target_id: UUID
    target_type: str
    target_display_name: str

class Browse(BaseModel):
    target_type: str
    target_id: UUID
    target_name: str
    target_theme: str
    params: dict[str, Any]
    href: str
    browse_theme: str
    metrics_info: MetricsInfo1
    type: str

class MetricsInfo2(BaseModel):
    target_id: UUID
    target_type: str
    target_display_name: str
    eab: str
    field_type: str = Field(..., alias='_type')

class Action(BaseModel):
    action_type: str
    entity_name: str
    entity_type: str
    metrics_info: MetricsInfo2
    eab: str

class Image1(BaseModel):
    path: str
    accent: Accent
    image_id: str

class Horizontal1(BaseModel):
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image1
    text: str

class Vertical(BaseModel):
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    text: str

class Artwork2(BaseModel):
    field_type: str = Field(..., alias='_type')
    horizontal: Horizontal1
    vertical: Vertical

class Browse1(BaseModel):
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    type: str

class Action1(BaseModel):
    action_type: str
    entity_name: str
    entity_type: str
    metrics_info: MetricsInfo2
    browse: Browse1
    target_name: str
    href: str

class BrandWatermarkBottomRight1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork3(BaseModel):
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_bottom_right: BrandLogoBottomRight1 = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding1(BaseModel):
    id: UUID
    name: str
    artwork: Artwork3

class Header(BaseModel):
    title: str
    artwork: Artwork2
    action: Action1
    primary_branding: PrimaryBranding1 | None = None

class ContextMenu(BaseModel):
    actions: list[Action]
    header: Header

class Availability(BaseModel):
    field_type: str = Field(..., alias='_type')
    start_date: AwareDatetime
    end_date: AwareDatetime
    location_requirement: str
    is_available: bool

class Rights(BaseModel):
    startover: bool
    recordable: bool
    offline: bool
    client_override: bool
    co_viewing: bool

class Bundle(BaseModel):
    field_type: str = Field(..., alias='_type')
    id: int
    eab_id: str
    network_id: UUID
    network_name: str
    duration: int
    availability: Availability
    bundle_type: str
    rating: str
    open_credit_end_pos: int
    close_credit_start_pos: int
    rights: Rights
    cp_id: int
    all_etag: str
    rights_etag: str
    airings_etag: str
    stream_etag: str
    rights_ttl: int
    airings_ttl: int
    stream_ttl: int
    package_id: int
    av_features: list[None]

class MetricsInfo4(BaseModel):
    target_id: UUID
    target_type: str
    target_display_name: str
    eab: str
    airing_type: str

class Playback(BaseModel):
    eab: str
    bundle: Bundle
    metrics_info: MetricsInfo4
    type: str

class Actions(BaseModel):
    browse: Browse
    context_menu: ContextMenu
    playback: Playback | None = None

class Rating(BaseModel):
    code: str | None = None

class EntityMetadata(BaseModel):
    genre_names: list[str]
    premiere_date: AwareDatetime
    rating: Rating
    target_name: str
    is_warm: bool
    network_name: str | None = None
    availability: Availability | None = None

class Result(BaseModel):
    field_type: str = Field(..., alias='_type')
    metrics_info: MetricsInfo
    personalization: Personalization
    device_context_failure: bool
    view_template: str
    visuals: Visuals
    actions: Actions
    entity_metadata: EntityMetadata

class Group(BaseModel):
    category: str
    results: list[Result]

class Metadata(BaseModel):
    search_result_type: str
    explanation: str
    selection_tracking_id: UUID

class SearchModel(BaseModel):
    groups: list[Group]
    metadata: Metadata
    device_context_failure: bool
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
