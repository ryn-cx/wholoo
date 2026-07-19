from uuid import UUID
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from typing import Any

class MetricsInfo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    target_id: UUID
    target_type: str
    target_name: str
    selection_tracking_id: UUID

class Personalization(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bowie_context: str
    eab: str

class Accent(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    hue: int
    classification: str

class Image(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_id: str

class Horizontal(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image
    text: str

class Artwork(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    horizontal: Horizontal

class Headline(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text: str
    index: list[list[int]]

class Body(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text: str
    index: list[list[int]]

class BrandWatermarkBottomRight(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_bottom_right: BrandLogoBottomRight = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    name: str
    artwork: Artwork1

class ShortSubtitle(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text: str
    index: list[None]

class Visuals(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    artwork: Artwork
    headline: Headline
    body: Body | None = None
    action_text: str
    primary_branding: PrimaryBranding | None = None
    short_subtitle: ShortSubtitle

class Params(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    network_breadcrumb: UUID | None = None

class MetricsInfo1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    action_type: str
    target_id: UUID
    target_type: str
    target_display_name: str

class Browse(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    target_type: str
    target_id: UUID
    target_name: str
    target_theme: str
    params: Params
    href: str
    browse_theme: str
    metrics_info: MetricsInfo1
    type: str

class MetricsInfo2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    target_id: UUID
    target_type: str
    target_display_name: str
    eab: str
    field_type: str = Field(..., alias='_type')

class Action(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    action_type: str
    entity_name: str
    entity_type: str
    metrics_info: MetricsInfo2
    eab: str

class Image1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_id: str

class Horizontal1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    image: Image1
    text: str

class Vertical(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    artwork_type: str
    text: str

class Artwork2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    horizontal: Horizontal1
    vertical: Vertical

class BrandWatermarkBottomRight1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_bottom_right: BrandLogoBottomRight1 = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    name: str
    artwork: Artwork3

class Browse1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    target_type: str
    target_id: UUID
    target_theme: str
    params: Params
    type: str

class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    action_type: str
    entity_name: str
    entity_type: str
    metrics_info: MetricsInfo2
    browse: Browse1
    target_name: str
    href: str

class Header(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    artwork: Artwork2
    primary_branding: PrimaryBranding1 | None = None
    action: Action1

class ContextMenu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    actions: list[Action]
    header: Header

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    start_date: AwareDatetime
    end_date: AwareDatetime
    location_requirement: str
    is_available: bool

class Rights(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    startover: bool
    recordable: bool
    offline: bool
    client_override: bool
    co_viewing: bool

class Bundle(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: int
    eab_id: str
    network_id: UUID
    network_name: str
    duration: int
    availability: Availability
    bundle_type: str
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
    rating: str | None = None

class MetricsInfo4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    target_id: UUID
    target_type: str
    target_display_name: str
    eab: str
    airing_type: str

class Playback(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    eab: str
    bundle: Bundle
    metrics_info: MetricsInfo4
    type: str

class Actions(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    browse: Browse
    context_menu: ContextMenu
    playback: Playback | None = None

class Rating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str | None = None

class EntityMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    genre_names: list[str] | None = None
    premiere_date: AwareDatetime | None = None
    rating: Rating | None = None
    target_name: str
    is_warm: bool
    network_name: str | None = None
    availability: Availability | None = None

class Result(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    metrics_info: MetricsInfo
    personalization: Personalization
    device_context_failure: bool
    view_template: str
    visuals: Visuals
    actions: Actions
    entity_metadata: EntityMetadata

class Group(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    category: str
    results: list[Result]

class Metadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    search_result_type: str
    explanation: str
    selection_tracking_id: UUID

class SearchModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    groups: list[Group]
    metadata: Metadata
    device_context_failure: bool
