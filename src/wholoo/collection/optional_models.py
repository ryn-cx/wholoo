from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID
from typing import Any

class Personalization(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bowie_context: str | None = None

class ExternalIdentifier(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    namespace: str | None = None
    id: UUID | str | None = Field(default=None, union_mode='left_to_right')

class MetricsInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | None = None
    target_type: str | None = None
    target_name: str | None = None
    promo_text_format: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None

class Personalization1(BaseModel):
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

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class Vertical(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image1 | None = None
    text: str | None = None

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class HorizontalTile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image2 | None = None
    text: str | None = None

class Image3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class VerticalTile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image3 | None = None
    text: str | None = None

class Image4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class HorizontalVideo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image4 | None = None
    text: str | None = None

class Image5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None

class VerticalVideo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image5 | None = None
    text: str | None = None

class Image6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class HorizontalTitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image6 | None = None
    text: str | None = None

class Image7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class VerticalTitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image7 | None = None
    text: str | None = None

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    horizontal: Horizontal | None = None
    vertical: Vertical | None = None
    horizontal_tile: HorizontalTile | None = None
    vertical_tile: VerticalTile | None = None
    horizontal_video: HorizontalVideo | None = None
    vertical_video: VerticalVideo | None = None
    horizontal_title: HorizontalTitle | None = None
    vertical_title: VerticalTitle | None = None

class BrandWatermark(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkBottomRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark | None = Field(None, alias='brand.watermark')
    brand_logo: BrandLogo | None = Field(None, alias='brand.logo')
    brand_watermark_bottom_right: BrandWatermarkBottomRight | None = Field(None, alias='brand.watermark.bottom.right')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None
    artwork: Artwork1 | None = None

class Visuals(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    artwork: Artwork | None = None
    headline: str | None = None
    action_text: str | None = None
    body: str | None = None
    short_descriptor: str | None = None
    primary_branding: PrimaryBranding | None = None

class MetricsInfo1(BaseModel):
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
    metrics_info: MetricsInfo1 | None = None
    eab: str | None = None

class Image8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_id: str | None = None

class Horizontal1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image8 | None = None
    text: str | None = None

class Vertical1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    text: str | None = None

class Artwork2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    horizontal: Horizontal1 | None = None
    vertical: Vertical1 | None = None

class Browse(BaseModel):
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
    metrics_info: MetricsInfo1 | None = None
    browse: Browse | None = None
    target_name: str | None = None
    href: str | None = None

class BrandWatermark1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkTopRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class NetworkTile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkBottomRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogoTopRight(BaseModel):
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

class BrandWatermarkDark(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark1 | None = Field(None, alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo1 | None = Field(None, alias='brand.logo')
    network_tile: NetworkTile | None = Field(None, alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 | None = Field(None, alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight | None = Field(None, alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark | None = Field(None, alias='brand.watermark.dark')

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

class ModifyMyStuff(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entity_id: UUID | None = None
    entity_type: str | None = None
    entity_name: str | None = None
    eab: str | None = None
    metrics_info: MetricsInfo1 | None = None
    type: str | None = None

class Feedback(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | None = None
    target_type: str | None = None
    related_feedback_href: str | None = None
    display_entity_text: str | None = None
    type: str | None = None

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | None = None
    target_type: str | None = None
    target_display_name: str | None = None
    field_type: str | None = Field(None, alias='_type')

class StopSuggestingThis(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entity_id: UUID | None = None
    entity_type: str | None = None
    display_entity_text: str | None = None
    metrics_info: MetricsInfo4 | None = None
    type: str | None = None

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
    av_features: list[str] | None = None

class MetricsInfo5(BaseModel):
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
    metrics_info: MetricsInfo5 | None = None
    type: str | None = None

class MetricsInfo6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = None
    target_id: UUID | None = None
    target_type: str | None = None
    target_display_name: str | None = None

class Browse0(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: UUID | None = None
    target_name: str | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    href: str | None = None
    browse_theme: str | None = None
    metrics_info: MetricsInfo6 | None = None
    type: str | None = None

class Browse1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: UUID | None = None
    target_name: str | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    href: str | None = None
    browse_theme: str | None = None
    metrics_info: MetricsInfo6 | None = None
    type: str | None = None

class Params(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    network_breadcrumb: UUID | None = None

class NetworkBrowse(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: UUID | None = None
    target_name: str | None = None
    target_theme: str | None = None
    params: Params | None = None
    href: str | None = None
    browse_theme: str | None = None
    metrics_info: MetricsInfo6 | None = None
    type: str | None = None

class Browse11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: UUID | None = None
    target_name: str | None = None
    target_theme: str | None = None
    params: Params | None = None
    href: str | None = None
    browse_theme: str | None = None
    metrics_info: MetricsInfo6 | None = None
    type: str | None = None

class Actions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    context_menu: ContextMenu | None = None
    modify_my_stuff: ModifyMyStuff | None = None
    feedback: Feedback | None = None
    stop_suggesting_this: StopSuggestingThis | None = None
    playback: Playback | None = None
    browse_0: Browse0 | None = Field(None, alias='browse.0')
    browse: Browse1 | None = None
    network_browse: NetworkBrowse | None = None
    browse_1: Browse11 | None = Field(None, alias='browse.1')

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None

class EntityMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genre_names: list[str] | None = None
    premiere_date: AwareDatetime | None = None
    rating: Rating | None = None
    entity_type: str | None = None
    is_warm: bool | None = None

class CampaignMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_campaign: bool | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    metrics_info: MetricsInfo | None = None
    personalization: Personalization1 | None = None
    device_context_failure: bool | None = None
    view_template: str | None = None
    visuals: Visuals | None = None
    actions: Actions | None = None
    actions_ordering: list[str] | None = None
    entity_metadata: EntityMetadata | None = None
    campaign_metadata: CampaignMetadata | None = None

class Image9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None

class Horizontal2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image9 | None = None
    text: str | None = None

class Image10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None

class Vertical2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image10 | None = None
    text: str | None = None

class Artwork4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    horizontal: Horizontal2 | None = None
    vertical: Vertical2 | None = None

class Browse2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: str | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    type: str | None = None

class HubLink(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    href: str | None = None
    name: str | None = None
    theme: str | None = None
    artwork: Artwork4 | None = None
    browse: Browse2 | None = None

class Image11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None

class Horizontal3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image11 | None = None
    text: str | None = None

class Image12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None

class Vertical3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    artwork_type: str | None = None
    image: Image12 | None = None
    text: str | None = None

class Artwork5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    horizontal: Horizontal3 | None = None
    vertical: Vertical3 | None = None

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    href: str | None = None
    name: str | None = None
    theme: str | None = None
    artwork: Artwork5 | None = None
    browse: Browse2 | None = None
    position: int | None = None

class Pagination(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next: str | None = None
    current_offset: int | None = None
    previous: str | None = None

class CollectionModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    href: str | None = None
    p13n_href: str | None = None
    name: str | None = None
    theme: str | None = None
    description: str | None = None
    artwork: dict[str, Any] | None = None
    personalization: Personalization | None = None
    device_context_failure: bool | None = None
    items: list[Item] | None = None
    hub_link: HubLink | None = None
    actions: list[Action2] | None = None
    pagination: Pagination | None = None
    is_fallback: bool | None = None
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
