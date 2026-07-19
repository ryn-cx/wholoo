from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from uuid import UUID
from typing import Any

class Accent(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    hue: int
    classification: str

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

class DetailVerticalHero(GAPIBaseModel):
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
    title_treatment_horizontal: TitleTreatmentHorizontal = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile = Field(..., alias='program.tile')
    detail_vertical_hero: DetailVerticalHero = Field(..., alias='detail.vertical.hero')
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

class VideoHorizontalHero(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailVerticalHero1(GAPIBaseModel):
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

class TitleTreatmentStacked(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_horizontal_hero: VideoHorizontalHero | None = Field(None, alias='video.horizontal.hero')
    detail_vertical_hero: DetailVerticalHero1 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero1 | None = Field(None, alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked | None = Field(None, alias='title.treatment.stacked')

class VideoHorizontalHero1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_horizontal_hero: VideoHorizontalHero1 = Field(..., alias='video.horizontal.hero')

class ExternalIdentifier(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    namespace: str
    id: str

class MetricsInfo1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier]

class Personalization(GAPIBaseModel):
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

class Rating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str

class DetailVerticalHero2(GAPIBaseModel):
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

class SeriesArtwork(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_vertical_hero: DetailVerticalHero2 = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal2 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile2 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile2 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero2 = Field(..., alias='detail.horizontal.hero')

class Item1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork2
    metrics_info: MetricsInfo1
    personalization: Personalization
    device_context_failure: bool
    browse: Browse1
    series_id: UUID
    series_name: str
    season: str
    season_short_display_name: str
    bundle: Bundle
    number: str
    rating: Rating
    genre_names: list[str]
    premiere_date: AwareDatetime
    duration: int
    is_first_run: bool
    series_artwork: SeriesArtwork
    restriction_level: str
    exclusivity: str
    actions: list[None]

class Pagination(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    current_offset: int
    total_count: int
    next: str | None = None

class SeriesGroupingMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    series_grouping_type: str
    season_number: int
    grouping_name: str = Field(..., alias='groupingName')
    unknown: bool

class MetricsInfo2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str | None = None
    airing_type: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None
    reco_tags: str | None = None
    selection_tracking_id: UUID | None = None

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

class DetailVerticalHero3(GAPIBaseModel):
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

class SeriesArtwork1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_vertical_hero: DetailVerticalHero3 = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal3 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile3 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile3 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero3 = Field(..., alias='detail.horizontal.hero')

class BrandWatermark(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkTopRight(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class NetworkTile(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkBottomRight(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoTopRight(GAPIBaseModel):
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

class BrandWatermarkDark(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    brand_watermark: BrandWatermark | None = Field(None, alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo | None = Field(None, alias='brand.logo')
    network_tile: NetworkTile = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight = Field(..., alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark | None = Field(None, alias='brand.watermark.dark')

class PrimaryBranding(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    name: str
    artwork: Artwork3

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: str | UUID
    href: str
    p13n_href: str | None = None
    name: str
    theme: str | None = None
    artwork: Artwork1
    device_context_failure: bool
    items: list[Item1] | None = None
    pagination: Pagination | None = None
    series_grouping_metadata: SeriesGroupingMetadata | None = None
    description: str | None = None
    metrics_info: MetricsInfo2 | None = None
    personalization: Personalization | None = None
    browse: Browse1 | None = None
    series_id: UUID | None = None
    series_name: str | None = None
    season: str | None = None
    season_short_display_name: str | None = None
    bundle: Bundle1 | None = None
    number: str | None = None
    rating: Rating | None = None
    genre_names: list[str] | None = None
    premiere_date: AwareDatetime | None = None
    duration: int | None = None
    is_first_run: bool | None = None
    series_artwork: SeriesArtwork1 | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    actions: list[None] | None = None
    episodes: list[None] | None = None
    primary_branding: PrimaryBranding | None = None
    is_rolling: bool | None = None
    original_id: UUID | None = None
    original_type: str | None = None

class Pagination1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    current_offset: int

class FocusNavigation(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    collection_id: str
    entity_id: UUID

class Personalization2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bowie_context: str

class Component(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: str
    href: str
    name: str
    theme: str
    artwork: dict[str, Any]
    device_context_failure: bool
    items: list[Item]
    actions: list[None]
    pagination: Pagination1
    focus_navigation: FocusNavigation | None = None
    p13n_href: str | None = None
    personalization: Personalization2 | None = None
    is_fallback: bool | None = None

class VideoHorizontalHero2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_horizontal_hero: VideoHorizontalHero2 = Field(..., alias='video.horizontal.hero')

class MetricsInfo3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier]

class Personalization3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    eab: str

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

class DetailVerticalHero4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class SeriesArtwork2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_vertical_hero: DetailVerticalHero4 = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal4 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile4 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile4 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero4 = Field(..., alias='detail.horizontal.hero')

class Entity(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork4
    metrics_info: MetricsInfo3
    personalization: Personalization3
    device_context_failure: bool
    browse: Browse1
    series_id: UUID
    series_name: str
    season: str
    season_short_display_name: str
    bundle: Bundle2
    number: str
    rating: Rating
    genre_names: list[str]
    premiere_date: AwareDatetime
    duration: int
    is_first_run: bool
    series_artwork: SeriesArtwork2
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
    collection_id: int
    focus: Focus

class UserState(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    is_warm: bool
    is_cold: bool

class TitleTreatmentHorizontal5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailVerticalHero5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title_treatment_horizontal: TitleTreatmentHorizontal5 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile5 = Field(..., alias='program.tile')
    detail_vertical_hero: DetailVerticalHero5 = Field(..., alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile5 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero5 = Field(..., alias='detail.horizontal.hero')

class MetricsInfo5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    external_identifiers: list[ExternalIdentifier]

class BrandWatermark1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkTopRight1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogo1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class NetworkTile1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkBottomRight1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoTopRight1(GAPIBaseModel):
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

class Artwork6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    brand_watermark: BrandWatermark1 = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight1 = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo1 = Field(..., alias='brand.logo')
    network_tile: NetworkTile1 = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight1 = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight1 = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    name: str
    artwork: Artwork6

class Entity1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    p13n_href: str
    name: str
    description: str
    artwork: Artwork5
    metrics_info: MetricsInfo5
    personalization: Personalization3
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    episodes: list[None]
    primary_branding: PrimaryBranding1
    rating: Rating
    premiere_date: AwareDatetime
    restriction_level: str
    exclusivity: str
    is_rolling: bool
    actions: list[None]

class Item2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_text: str

class Credit(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    prefix: str
    items: list[Item2]

class Details(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    vod_items: VodItems
    user_state: UserState
    entity: Entity1
    credits: list[Credit]

class TVModel(GAPIBaseModel):
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
