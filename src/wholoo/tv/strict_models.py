from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID
from typing import Any

class Accent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hue: int
    classification: str

class TitleTreatmentHorizontal(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailVerticalHero(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentStacked(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_treatment_horizontal: TitleTreatmentHorizontal | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile = Field(..., alias='program.tile')
    detail_vertical_hero: DetailVerticalHero | None = Field(None, alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero = Field(..., alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked | None = Field(None, alias='title.treatment.stacked')
    video_horizontal_hero: VideoHorizontalHero | None = Field(None, alias='video.horizontal.hero')

class MetricsInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    page_type: str

class Browse(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    type: str

class DetailVerticalHero1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentStacked1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalWide(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_vertical_hero: DetailVerticalHero1 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero1 | None = Field(None, alias='detail.horizontal.hero')
    video_horizontal_hero: VideoHorizontalHero1 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked1 | None = Field(None, alias='title.treatment.stacked')
    detail_horizontal_wide: DetailHorizontalWide | None = Field(None, alias='detail.horizontal.wide')

class VideoHorizontalHero2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoVerticalHero(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_horizontal_hero: VideoHorizontalHero2 = Field(..., alias='video.horizontal.hero')
    program_tile: ProgramTile2 | None = Field(None, alias='program.tile')
    video_vertical_hero: VideoVerticalHero | None = Field(None, alias='video.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal2 | None = Field(None, alias='title.treatment.horizontal')

class ExternalIdentifier(BaseModel):
    model_config = ConfigDict(defer_build=True)
    namespace: str
    id: UUID | str = Field(union_mode='left_to_right')

class MetricsInfo1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier] | None = None

class Personalization(BaseModel):
    model_config = ConfigDict(defer_build=True)
    eab: str

class Browse1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    href: str
    browse_theme: str
    type: str

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    start_date: AwareDatetime
    end_date: AwareDatetime | None = None
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

class Rating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str | None = None

class DetailVerticalHero2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentStacked2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class SeriesArtwork(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_vertical_hero: DetailVerticalHero2 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal3 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile3 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile2 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero2 | None = Field(None, alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked2 | None = Field(None, alias='title.treatment.stacked')
    video_horizontal_hero: VideoHorizontalHero3 | None = Field(None, alias='video.horizontal.hero')

class BrandWatermark(BaseModel):
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

class BrandLogo(BaseModel):
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

class BrandWatermarkBottomRight(BaseModel):
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

class ProgramTile4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandHubBackground(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo = Field(..., alias='brand.logo')
    network_tile: NetworkTile = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight = Field(..., alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark | None = Field(None, alias='brand.watermark.dark')
    program_tile: ProgramTile4 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile3 | None = Field(None, alias='program.vertical.tile')
    brand_hub_background: BrandHubBackground | None = Field(None, alias='brand.hub.background')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork3

class Item1(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    season_short_display_name: str | None = None
    bundle: Bundle
    number: str
    rating: Rating
    genre_names: list[str]
    premiere_date: AwareDatetime | None = None
    duration: int | None = None
    is_first_run: bool
    series_artwork: SeriesArtwork
    restriction_level: str
    exclusivity: str
    actions: list[None]
    primary_branding: PrimaryBranding | None = None

class Pagination(BaseModel):
    model_config = ConfigDict(defer_build=True)
    current_offset: int
    total_count: int
    next: str | None = None

class SeriesGroupingMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    series_grouping_type: str
    season_number: int
    grouping_name: str = Field(..., alias='groupingName')
    unknown: bool

class MetricsInfo2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    reco_tags: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None
    selection_tracking_id: UUID | None = None
    metrics_asset_name: str | None = None
    airing_type: str | None = None

class BrandWatermark1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkTopRight1(BaseModel):
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

class NetworkTile1(BaseModel):
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

class BrandLogoTopRight1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkDark1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandHubBackground1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark1 | None = Field(None, alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight1 | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo1 | None = Field(None, alias='brand.logo')
    network_tile: NetworkTile1 | None = Field(None, alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 | None = Field(None, alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight1 | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight1 | None = Field(None, alias='brand.logo.bottom.right')
    program_tile: ProgramTile5 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile4 | None = Field(None, alias='program.vertical.tile')
    brand_watermark_dark: BrandWatermarkDark1 | None = Field(None, alias='brand.watermark.dark')
    brand_hub_background: BrandHubBackground1 | None = Field(None, alias='brand.hub.background')

class PrimaryBranding1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork4

class Bundle1(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    av_features: list[str]
    rating: str | None = None

class DetailVerticalHero3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class SeriesArtwork1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_vertical_hero: DetailVerticalHero3 = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal4 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile6 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile5 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero3 = Field(..., alias='detail.horizontal.hero')

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: UUID | str = Field(union_mode='left_to_right')
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
    genre_names: list[str] | None = None
    episodes: list[None] | None = None
    rating: Rating | None = None
    premiere_date: AwareDatetime | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    is_rolling: bool | None = None
    actions: list[None] | None = None
    primary_branding: PrimaryBranding1 | None = None
    duration: int | None = None
    original_id: UUID | None = None
    original_type: str | None = None
    relationship: str | None = None
    bundle: Bundle1 | None = None
    series_id: UUID | None = None
    series_name: str | None = None
    season: str | None = None
    season_short_display_name: str | None = None
    number: str | None = None
    is_first_run: bool | None = None
    series_artwork: SeriesArtwork1 | None = None

class Pagination1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    current_offset: int

class FocusNavigation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    collection_id: str
    entity_id: UUID

class Personalization2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bowie_context: str

class Component(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    description: str | None = None

class VideoHorizontalHero4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoVerticalHero1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_horizontal_hero: VideoHorizontalHero4 = Field(..., alias='video.horizontal.hero')
    program_tile: ProgramTile7 | None = Field(None, alias='program.tile')
    video_vertical_hero: VideoVerticalHero1 | None = Field(None, alias='video.vertical.hero')

class MetricsInfo3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier] | None = None

class Personalization3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    eab: str

class Bundle2(BaseModel):
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

class DetailVerticalHero4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentStacked3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class SeriesArtwork2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_vertical_hero: DetailVerticalHero4 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal5 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile8 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile6 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero4 | None = Field(None, alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked3 | None = Field(None, alias='title.treatment.stacked')
    video_horizontal_hero: VideoHorizontalHero5 | None = Field(None, alias='video.horizontal.hero')

class BrandWatermark2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkTopRight2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogo2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class NetworkTile2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkBottomRight2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoTopRight2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkDark2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandHubBackground2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark2 = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight2 = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo2 = Field(..., alias='brand.logo')
    network_tile: NetworkTile2 = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight2 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight2 = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight2 = Field(..., alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark2 | None = Field(None, alias='brand.watermark.dark')
    program_tile: ProgramTile9 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile7 | None = Field(None, alias='program.vertical.tile')
    brand_hub_background: BrandHubBackground2 | None = Field(None, alias='brand.hub.background')

class PrimaryBranding2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork6

class Entity(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork5
    metrics_info: MetricsInfo3
    personalization: Personalization3
    device_context_failure: bool
    browse: Browse1
    series_id: UUID
    series_name: str
    season: str
    season_short_display_name: str | None = None
    bundle: Bundle2
    number: str
    rating: Rating
    genre_names: list[str]
    premiere_date: AwareDatetime | None = None
    duration: int | None = None
    is_first_run: bool
    series_artwork: SeriesArtwork2
    restriction_level: str
    exclusivity: str
    primary_branding: PrimaryBranding2 | None = None

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    reco_tags: str
    selection_tracking_id: UUID

class Focus(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    entity: Entity
    action_text: str
    metrics_info: MetricsInfo4

class VodItems(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: str
    collection_id: int
    focus: Focus

class UserState(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    is_warm: bool
    is_cold: bool

class TitleTreatmentHorizontal6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailVerticalHero5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentStacked4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_treatment_horizontal: TitleTreatmentHorizontal6 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile10 = Field(..., alias='program.tile')
    detail_vertical_hero: DetailVerticalHero5 | None = Field(None, alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile8 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero5 = Field(..., alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked4 | None = Field(None, alias='title.treatment.stacked')
    video_horizontal_hero: VideoHorizontalHero6 | None = Field(None, alias='video.horizontal.hero')

class ExternalIdentifier3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    namespace: str
    id: str

class MetricsInfo5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    external_identifiers: list[ExternalIdentifier3]

class BrandWatermark3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkTopRight3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogo3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class NetworkTile3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkBottomRight3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoTopRight3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkDark3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandHubBackground3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark3 | None = Field(None, alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight3 | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo3 | None = Field(None, alias='brand.logo')
    program_tile: ProgramTile11 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile9 | None = Field(None, alias='program.vertical.tile')
    network_tile: NetworkTile3 = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight3 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight3 | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight3 | None = Field(None, alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark3 | None = Field(None, alias='brand.watermark.dark')
    brand_hub_background: BrandHubBackground3 | None = Field(None, alias='brand.hub.background')

class PrimaryBranding3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork8

class Entity1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    p13n_href: str
    name: str
    description: str
    artwork: Artwork7
    metrics_info: MetricsInfo5 | None = None
    personalization: Personalization3
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    episodes: list[None]
    rating: Rating
    premiere_date: AwareDatetime | None = None
    restriction_level: str
    exclusivity: str
    is_rolling: bool
    actions: list[None]
    primary_branding: PrimaryBranding3 | None = None

class Item2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display_text: str

class Credit(BaseModel):
    model_config = ConfigDict(defer_build=True)
    prefix: str
    items: list[Item2]

class Details(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    vod_items: VodItems
    user_state: UserState
    entity: Entity1
    credits: list[Credit]

class TVModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
