from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from uuid import UUID
from typing import Any

class Accent(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    hue: int
    classification: str

class DetailVerticalHero(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_vertical_hero: DetailVerticalHero = Field(..., alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero = Field(..., alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero = Field(..., alias='detail.horizontal.hero')

class MetricsInfo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    page_type: str

class Browse(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    type: str

class Personalization(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bowie_context: str

class DetailVerticalHero1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_vertical_hero: DetailVerticalHero1 | None = Field(None, alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero1 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero1 | None = Field(None, alias='detail.horizontal.hero')

class ExternalIdentifier(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    namespace: str
    id: str

class MetricsInfo1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    reco_tags: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None
    selection_tracking_id: UUID | None = None
    metrics_asset_name: str | None = None
    airing_type: str | None = None

class Personalization1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    eab: str

class Browse1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    href: str
    browse_theme: str
    type: str

class Rating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str

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
    av_features: list[str]

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork1
    metrics_info: MetricsInfo1
    personalization: Personalization1
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    rating: Rating
    premiere_date: AwareDatetime
    duration: int | None = None
    restriction_level: str
    exclusivity: str | None = None
    actions: list[None]
    original_id: UUID | None = None
    original_type: str | None = None
    relationship: str | None = None
    bundle: Bundle | None = None

class Pagination(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    current_offset: int

class Component(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: str
    href: str
    p13n_href: str
    name: str
    theme: str
    artwork: dict[str, Any]
    personalization: Personalization
    device_context_failure: bool
    items: list[Item]
    actions: list[None]
    pagination: Pagination
    is_fallback: bool

class VideoHorizontalHero2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_horizontal_hero: VideoHorizontalHero2 = Field(..., alias='video.horizontal.hero')

class MetricsInfo2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str

class Bundle1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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
    av_features: list[str]

class Trailer(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork2
    metrics_info: MetricsInfo2
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    original_id: UUID
    original_type: str
    rating: Rating
    premiere_date: AwareDatetime
    relationship: str
    bundle: Bundle1
    restriction_level: str
    actions: list[None]

class DetailVerticalHero2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_vertical_hero: DetailVerticalHero2 = Field(..., alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero3 = Field(..., alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal2 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile2 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile2 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero2 = Field(..., alias='detail.horizontal.hero')

class MetricsInfo3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier]

class Bundle2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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
    av_features: list[str]

class Entity(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork3
    metrics_info: MetricsInfo3
    personalization: Personalization1
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    bundle: Bundle2
    rating: Rating
    premiere_date: AwareDatetime
    duration: int
    restriction_level: str
    exclusivity: str

class MetricsInfo4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    reco_tags: str
    selection_tracking_id: UUID

class Focus(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    entity: Entity
    action_text: str
    metrics_info: MetricsInfo4

class VodItems(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: str
    focus: Focus

class UserState(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    is_warm: bool
    is_cold: bool

class DetailVerticalHero3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_vertical_hero: DetailVerticalHero3 = Field(..., alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero4 = Field(..., alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal3 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile3 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile3 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero3 = Field(..., alias='detail.horizontal.hero')

class MetricsInfo5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    external_identifiers: list[ExternalIdentifier]

class Entity1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    p13n_href: str
    name: str
    description: str
    artwork: Artwork4
    metrics_info: MetricsInfo5
    personalization: Personalization1
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    rating: Rating
    premiere_date: AwareDatetime
    duration: int
    restriction_level: str
    exclusivity: str
    actions: list[None]

class Item1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_text: str

class Credit(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    prefix: str
    items: list[Item1]

class Details(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    trailer: Trailer
    vod_items: VodItems
    user_state: UserState
    entity: Entity1
    credits: list[Credit]

class MoviesModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    theme: str
    artwork: Artwork
    metrics_info: MetricsInfo
    device_context_failure: bool
    browse: Browse
    components: list[Component]
    details: Details
    actions: list[None]
