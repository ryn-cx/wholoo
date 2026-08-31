from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID
from typing import Any

class Personalization(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bowie_context: str

class ExternalIdentifier(BaseModel):
    model_config = ConfigDict(defer_build=True)
    namespace: str
    id: UUID | str = Field(union_mode='left_to_right')

class MetricsInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_id: UUID
    target_type: str
    target_name: str
    promo_text_format: str
    external_identifiers: list[ExternalIdentifier] | None = None

class Personalization1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bowie_context: str
    eab: str

class Accent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hue: int
    classification: str

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_id: str

class Horizontal(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image
    text: str

class Image1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_id: str

class Vertical(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image1
    text: str

class Image2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_id: str

class HorizontalTile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image2
    text: str

class Image3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_id: str

class VerticalTile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image3
    text: str

class Image4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_id: str | None = None

class HorizontalVideo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image4
    text: str

class Image5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent

class VerticalVideo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image5
    text: str

class Image6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_id: str

class HorizontalTitle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image6
    text: str

class Image7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_id: str

class VerticalTitle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image7
    text: str

class Artwork(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    horizontal: Horizontal
    vertical: Vertical
    horizontal_tile: HorizontalTile
    vertical_tile: VerticalTile
    horizontal_video: HorizontalVideo
    vertical_video: VerticalVideo
    horizontal_title: HorizontalTitle | None = None
    vertical_title: VerticalTitle | None = None

class BrandWatermark(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkBottomRight(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark = Field(..., alias='brand.watermark')
    brand_logo: BrandLogo = Field(..., alias='brand.logo')
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork1

class Visuals(BaseModel):
    model_config = ConfigDict(defer_build=True)
    artwork: Artwork
    headline: str
    action_text: str
    body: str
    short_descriptor: str
    primary_branding: PrimaryBranding | None = None

class MetricsInfo1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_id: UUID
    target_type: str
    target_display_name: str
    eab: str
    field_type: str = Field(..., alias='_type')

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str
    entity_name: str
    entity_type: str
    metrics_info: MetricsInfo1
    eab: str

class Image8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_id: str

class Horizontal1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image8
    text: str

class Vertical1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    text: str

class Artwork2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    horizontal: Horizontal1
    vertical: Vertical1

class Browse(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    type: str

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str
    entity_name: str
    entity_type: str
    metrics_info: MetricsInfo1
    browse: Browse
    target_name: str
    href: str

class BrandWatermark1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkTopRight(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogo1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class NetworkTile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkBottomRight1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoTopRight(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkDark(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark1 = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo1 = Field(..., alias='brand.logo')
    network_tile: NetworkTile = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight = Field(..., alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark | None = Field(None, alias='brand.watermark.dark')

class PrimaryBranding1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork3

class Header(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    artwork: Artwork2
    action: Action1
    primary_branding: PrimaryBranding1 | None = None

class ContextMenu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action]
    header: Header

class ModifyMyStuff(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entity_id: UUID
    entity_type: str
    entity_name: str
    eab: str
    metrics_info: MetricsInfo1
    type: str

class Feedback(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_id: UUID
    target_type: str
    related_feedback_href: str
    display_entity_text: str
    type: str

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_id: UUID
    target_type: str
    target_display_name: str
    field_type: str = Field(..., alias='_type')

class StopSuggestingThis(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entity_id: UUID
    entity_type: str
    display_entity_text: str
    metrics_info: MetricsInfo4
    type: str

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    start_date: AwareDatetime
    end_date: AwareDatetime
    location_requirement: str
    is_available: bool

class Rights(BaseModel):
    model_config = ConfigDict(defer_build=True)
    startover: bool
    recordable: bool
    offline: bool
    client_override: bool
    co_viewing: bool

class Bundle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: int
    eab_id: str
    network_id: UUID
    network_name: str
    duration: int
    availability: Availability
    bundle_type: str
    rating: str | None = None
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
    av_features: list[str]

class MetricsInfo5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_id: UUID
    target_type: str
    target_display_name: str
    eab: str
    airing_type: str

class Playback(BaseModel):
    model_config = ConfigDict(defer_build=True)
    eab: str
    bundle: Bundle
    metrics_info: MetricsInfo5
    type: str

class MetricsInfo6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str
    target_id: UUID
    target_type: str
    target_display_name: str

class Browse0(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_type: str
    target_id: UUID
    target_name: str
    target_theme: str
    params: dict[str, Any]
    href: str
    browse_theme: str
    metrics_info: MetricsInfo6
    type: str

class Browse1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_type: str
    target_id: UUID
    target_name: str
    target_theme: str
    params: dict[str, Any]
    href: str
    browse_theme: str
    metrics_info: MetricsInfo6
    type: str

class Params(BaseModel):
    model_config = ConfigDict(defer_build=True)
    network_breadcrumb: UUID

class NetworkBrowse(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_type: str
    target_id: UUID
    target_name: str
    target_theme: str
    params: Params
    href: str
    browse_theme: str
    metrics_info: MetricsInfo6
    type: str

class Browse11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_type: str
    target_id: UUID
    target_name: str
    target_theme: str
    params: Params
    href: str
    browse_theme: str
    metrics_info: MetricsInfo6
    type: str

class Actions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    context_menu: ContextMenu
    modify_my_stuff: ModifyMyStuff
    feedback: Feedback
    stop_suggesting_this: StopSuggestingThis
    playback: Playback
    browse_0: Browse0 = Field(..., alias='browse.0')
    browse: Browse1
    network_browse: NetworkBrowse | None = None
    browse_1: Browse11 | None = Field(None, alias='browse.1')

class Rating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str | None = None

class EntityMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    genre_names: list[str]
    premiere_date: AwareDatetime
    rating: Rating
    entity_type: str
    is_warm: bool

class CampaignMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_campaign: bool

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: UUID
    metrics_info: MetricsInfo
    personalization: Personalization1
    device_context_failure: bool
    view_template: str
    visuals: Visuals
    actions: Actions
    actions_ordering: list[str]
    entity_metadata: EntityMetadata
    campaign_metadata: CampaignMetadata

class Image9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent

class Horizontal2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image9
    text: str

class Image10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent

class Vertical2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image10
    text: str

class Artwork4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    horizontal: Horizontal2
    vertical: Vertical2

class Browse2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_type: str
    target_id: str
    target_theme: str
    params: dict[str, Any]
    type: str

class HubLink(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: str
    href: str
    name: str
    theme: str
    artwork: Artwork4
    browse: Browse2

class Image11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent

class Horizontal3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image11
    text: str

class Image12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent

class Vertical3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image12
    text: str

class Artwork5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    horizontal: Horizontal3
    vertical: Vertical3

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: str
    href: str | None = None
    name: str
    theme: str | None = None
    artwork: Artwork5 | None = None
    browse: Browse2 | None = None
    position: int | None = None

class Pagination(BaseModel):
    model_config = ConfigDict(defer_build=True)
    next: str | None = None
    current_offset: int
    previous: str | None = None

class CollectionModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: str
    href: str
    p13n_href: str
    name: str
    theme: str
    description: str | None = None
    artwork: dict[str, Any]
    personalization: Personalization
    device_context_failure: bool
    items: list[Item]
    hub_link: HubLink
    actions: list[Action2]
    pagination: Pagination
    is_fallback: bool
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
