from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID
from typing import Any

class Accent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hue: int | None = None
    classification: str | None = None

class TitleTreatmentHorizontal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailVerticalHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentStacked(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_treatment_horizontal: TitleTreatmentHorizontal | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile | None = Field(None, alias='program.tile')
    detail_vertical_hero: DetailVerticalHero | None = Field(None, alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero | None = Field(None, alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked | None = Field(None, alias='title.treatment.stacked')

class MetricsInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    page_type: str | None = None

class Browse(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: UUID | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    type: str | None = None

class DetailVerticalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class VideoHorizontalHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentStacked1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalWide(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_vertical_hero: DetailVerticalHero1 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero1 | None = Field(None, alias='detail.horizontal.hero')
    video_horizontal_hero: VideoHorizontalHero | None = Field(None, alias='video.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked1 | None = Field(None, alias='title.treatment.stacked')
    detail_horizontal_wide: DetailHorizontalWide | None = Field(None, alias='detail.horizontal.wide')

class VideoHorizontalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_horizontal_hero: VideoHorizontalHero1 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal2 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile2 | None = Field(None, alias='program.tile')

class ExternalIdentifier(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    namespace: str | None = None
    id: str | None = None

class MetricsInfo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    metrics_asset_name: str | None = None
    airing_type: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None

class Personalization(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eab: str | None = None

class Browse1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | None = None
    target_id: UUID | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    href: str | None = None
    browse_theme: str | None = None
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

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None

class DetailVerticalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentStacked2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class SeriesArtwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_vertical_hero: DetailVerticalHero2 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal3 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile3 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile2 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero2 | None = Field(None, alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked2 | None = Field(None, alias='title.treatment.stacked')

class BrandWatermark(BaseModel):
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

class BrandWatermarkTopRight(BaseModel):
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

class ProgramTile4(BaseModel):
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

class ProgramVerticalTile3(BaseModel):
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

class BrandHubBackground(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark | None = Field(None, alias='brand.watermark')
    brand_watermark_dark: BrandWatermarkDark | None = Field(None, alias='brand.watermark.dark')
    brand_watermark_top_right: BrandWatermarkTopRight | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo | None = Field(None, alias='brand.logo')
    program_tile: ProgramTile4 | None = Field(None, alias='program.tile')
    network_tile: NetworkTile | None = Field(None, alias='network.tile')
    program_vertical_tile: ProgramVerticalTile3 | None = Field(None, alias='program.vertical.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight | None = Field(None, alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight | None = Field(None, alias='brand.logo.bottom.right')
    brand_hub_background: BrandHubBackground | None = Field(None, alias='brand.hub.background')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None
    artwork: Artwork3 | None = None

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    name: str | None = None
    description: str | None = None
    artwork: Artwork2 | None = None
    metrics_info: MetricsInfo1 | None = None
    personalization: Personalization | None = None
    device_context_failure: bool | None = None
    browse: Browse1 | None = None
    series_id: UUID | None = None
    series_name: str | None = None
    season: str | None = None
    season_short_display_name: str | None = None
    bundle: Bundle | None = None
    number: str | None = None
    rating: Rating | None = None
    genre_names: list[str] | None = None
    premiere_date: AwareDatetime | None = None
    duration: int | None = None
    is_first_run: bool | None = None
    series_artwork: SeriesArtwork | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    actions: list[Any] | None = None
    primary_branding: PrimaryBranding | None = None

class Pagination(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    current_offset: int | None = None
    total_count: int | None = None
    next: str | None = None

class SeriesGroupingMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    series_grouping_type: str | None = None
    season_number: int | None = None
    grouping_name: str | None = Field(None, alias='groupingName')
    unknown: bool | None = None

class ExternalIdentifier1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    namespace: str | None = None
    id: UUID | str | None = Field(default=None, union_mode='left_to_right')

class MetricsInfo2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    reco_tags: str | None = None
    external_identifiers: list[ExternalIdentifier1] | None = None
    selection_tracking_id: UUID | None = None
    metrics_asset_name: str | None = None
    airing_type: str | None = None

class BrandWatermark1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkTopRight1(BaseModel):
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

class NetworkTile1(BaseModel):
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

class BrandLogoTopRight1(BaseModel):
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

class ProgramTile5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkDark1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandHubBackground1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
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
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None
    artwork: Artwork4 | None = None

class Bundle1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: int | None = None
    eab_id: str | None = None
    network_id: UUID | None = None
    network_name: str | None = None
    duration: int | None = None
    availability: Availability | None = None
    bundle_type: str | None = None
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
    rating: str | None = None

class DetailVerticalHero3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class SeriesArtwork1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_vertical_hero: DetailVerticalHero3 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal4 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile6 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile5 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero3 | None = Field(None, alias='detail.horizontal.hero')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: UUID | str | None = Field(default=None, union_mode='left_to_right')
    href: str | None = None
    p13n_href: str | None = None
    name: str | None = None
    theme: str | None = None
    artwork: Artwork1 | None = None
    device_context_failure: bool | None = None
    items: list[Item1] | None = None
    pagination: Pagination | None = None
    series_grouping_metadata: SeriesGroupingMetadata | None = None
    description: str | None = None
    metrics_info: MetricsInfo2 | None = None
    personalization: Personalization | None = None
    browse: Browse1 | None = None
    genre_names: list[str] | None = None
    episodes: list[Any] | None = None
    rating: Rating | None = None
    premiere_date: AwareDatetime | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    is_rolling: bool | None = None
    actions: list[Any] | None = None
    primary_branding: PrimaryBranding1 | None = None
    duration: int | None = None
    original_id: UUID | None = None
    original_type: str | None = None
    bundle: Bundle1 | None = None
    relationship: str | None = None
    series_id: UUID | None = None
    series_name: str | None = None
    season: str | None = None
    season_short_display_name: str | None = None
    number: str | None = None
    is_first_run: bool | None = None
    series_artwork: SeriesArtwork1 | None = None

class Pagination1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    current_offset: int | None = None

class FocusNavigation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_id: str | None = None
    entity_id: UUID | None = None

class Personalization2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bowie_context: str | None = None

class Component(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    href: str | None = None
    name: str | None = None
    theme: str | None = None
    artwork: dict[str, Any] | None = None
    device_context_failure: bool | None = None
    items: list[Item] | None = None
    actions: list[Any] | None = None
    pagination: Pagination1 | None = None
    focus_navigation: FocusNavigation | None = None
    p13n_href: str | None = None
    personalization: Personalization2 | None = None
    is_fallback: bool | None = None
    description: str | None = None

class VideoHorizontalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_horizontal_hero: VideoHorizontalHero2 | None = Field(None, alias='video.horizontal.hero')

class ExternalIdentifier2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    namespace: str | None = None
    id: str | None = None

class MetricsInfo3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    metrics_asset_name: str | None = None
    airing_type: str | None = None
    external_identifiers: list[ExternalIdentifier2] | None = None

class Personalization3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eab: str | None = None

class Bundle2(BaseModel):
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

class DetailVerticalHero4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentStacked3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class SeriesArtwork2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_vertical_hero: DetailVerticalHero4 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal5 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile7 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile6 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero4 | None = Field(None, alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked3 | None = Field(None, alias='title.treatment.stacked')

class BrandWatermark2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkDark2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkTopRight2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogo2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class NetworkTile2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkBottomRight2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogoTopRight2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogoBottomRight2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandHubBackground2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark2 | None = Field(None, alias='brand.watermark')
    brand_watermark_dark: BrandWatermarkDark2 | None = Field(None, alias='brand.watermark.dark')
    brand_watermark_top_right: BrandWatermarkTopRight2 | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo2 | None = Field(None, alias='brand.logo')
    program_tile: ProgramTile8 | None = Field(None, alias='program.tile')
    network_tile: NetworkTile2 | None = Field(None, alias='network.tile')
    program_vertical_tile: ProgramVerticalTile7 | None = Field(None, alias='program.vertical.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight2 | None = Field(None, alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight2 | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight2 | None = Field(None, alias='brand.logo.bottom.right')
    brand_hub_background: BrandHubBackground2 | None = Field(None, alias='brand.hub.background')

class PrimaryBranding2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None
    artwork: Artwork6 | None = None

class Entity(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    name: str | None = None
    description: str | None = None
    artwork: Artwork5 | None = None
    metrics_info: MetricsInfo3 | None = None
    personalization: Personalization3 | None = None
    device_context_failure: bool | None = None
    browse: Browse1 | None = None
    series_id: UUID | None = None
    series_name: str | None = None
    season: str | None = None
    season_short_display_name: str | None = None
    bundle: Bundle2 | None = None
    number: str | None = None
    rating: Rating | None = None
    genre_names: list[str] | None = None
    premiere_date: AwareDatetime | None = None
    duration: int | None = None
    is_first_run: bool | None = None
    series_artwork: SeriesArtwork2 | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    primary_branding: PrimaryBranding2 | None = None

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    reco_tags: str | None = None
    selection_tracking_id: UUID | None = None

class Focus(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    entity: Entity | None = None
    action_text: str | None = None
    metrics_info: MetricsInfo4 | None = None

class VodItems(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    collection_id: int | None = None
    focus: Focus | None = None

class UserState(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    is_warm: bool | None = None
    is_cold: bool | None = None

class TitleTreatmentHorizontal6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailVerticalHero5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentStacked4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_treatment_horizontal: TitleTreatmentHorizontal6 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile9 | None = Field(None, alias='program.tile')
    detail_vertical_hero: DetailVerticalHero5 | None = Field(None, alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile8 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero5 | None = Field(None, alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked4 | None = Field(None, alias='title.treatment.stacked')

class MetricsInfo5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    external_identifiers: list[ExternalIdentifier2] | None = None

class BrandWatermark3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkTopRight3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogo3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class NetworkTile3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandWatermarkBottomRight3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogoTopRight3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class BrandLogoBottomRight3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark3 | None = Field(None, alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight3 | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo3 | None = Field(None, alias='brand.logo')
    network_tile: NetworkTile3 | None = Field(None, alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight3 | None = Field(None, alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight3 | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight3 | None = Field(None, alias='brand.logo.bottom.right')
    program_tile: ProgramTile10 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile9 | None = Field(None, alias='program.vertical.tile')

class PrimaryBranding3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None
    artwork: Artwork8 | None = None

class Entity1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    p13n_href: str | None = None
    name: str | None = None
    description: str | None = None
    artwork: Artwork7 | None = None
    metrics_info: MetricsInfo5 | None = None
    personalization: Personalization3 | None = None
    device_context_failure: bool | None = None
    browse: Browse1 | None = None
    genre_names: list[str] | None = None
    episodes: list[Any] | None = None
    rating: Rating | None = None
    premiere_date: AwareDatetime | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    is_rolling: bool | None = None
    actions: list[Any] | None = None
    primary_branding: PrimaryBranding3 | None = None

class Item2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_text: str | None = None

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    prefix: str | None = None
    items: list[Item2] | None = None

class Details(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    vod_items: VodItems | None = None
    user_state: UserState | None = None
    entity: Entity1 | None = None
    credits: list[Credit] | None = None

class TVModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    name: str | None = None
    theme: str | None = None
    artwork: Artwork | None = None
    metrics_info: MetricsInfo | None = None
    device_context_failure: bool | None = None
    browse: Browse | None = None
    components: list[Component] | None = None
    details: Details | None = None
    actions: list[Any] | None = None
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
