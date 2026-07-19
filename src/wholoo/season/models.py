from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from uuid import UUID
from typing import Any

class Accent(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    hue: int
    classification: str

class VideoHorizontalHero(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_horizontal_hero: VideoHorizontalHero = Field(..., alias='video.horizontal.hero')

class ExternalIdentifier(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    namespace: str
    id: str

class MetricsInfo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier] | None = None

class Personalization(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    eab: str

class Browse(GAPIBaseModel):
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

class DetailVerticalHero(GAPIBaseModel):
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

class SeriesArtwork(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_vertical_hero: DetailVerticalHero = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero = Field(..., alias='detail.horizontal.hero')

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

class Artwork1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    brand_watermark: BrandWatermark = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo = Field(..., alias='brand.logo')
    network_tile: NetworkTile = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    name: str
    artwork: Artwork1

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork
    metrics_info: MetricsInfo
    personalization: Personalization
    device_context_failure: bool
    browse: Browse
    series_id: UUID
    series_name: str
    season: str
    season_short_display_name: str
    bundle: Bundle
    number: str
    rating: Rating
    genre_names: list[str]
    premiere_date: AwareDatetime
    duration: int | None = None
    is_first_run: bool
    series_artwork: SeriesArtwork
    restriction_level: str
    exclusivity: str
    actions: list[None]
    primary_branding: PrimaryBranding | None = None

class Pagination(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    current_offset: int
    total_count: int

class SeriesGroupingMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    series_grouping_type: str
    season_number: int
    grouping_name: str = Field(..., alias='groupingName')
    unknown: bool

class SeasonModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    id: str
    href: str
    p13n_href: str
    name: str
    theme: str
    artwork: dict[str, Any]
    device_context_failure: bool
    items: list[Item]
    pagination: Pagination
    series_grouping_metadata: SeriesGroupingMetadata
