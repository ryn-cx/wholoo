from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID
from typing import Any

class Accent(BaseModel):
    hue: int
    classification: str

class VideoHorizontalHero(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork(BaseModel):
    video_horizontal_hero: VideoHorizontalHero = Field(..., alias='video.horizontal.hero')

class ExternalIdentifier(BaseModel):
    namespace: str
    id: str

class MetricsInfo(BaseModel):
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier] | None = None

class Personalization(BaseModel):
    eab: str

class Browse(BaseModel):
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    href: str
    browse_theme: str
    type: str

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
    av_features: list[str]

class Rating(BaseModel):
    code: str

class DetailVerticalHero(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class SeriesArtwork(BaseModel):
    detail_vertical_hero: DetailVerticalHero = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero = Field(..., alias='detail.horizontal.hero')

class BrandWatermark(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkTopRight(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogo(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class NetworkTile(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkBottomRight(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoTopRight(BaseModel):
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
    brand_watermark: BrandWatermark = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo = Field(..., alias='brand.logo')
    network_tile: NetworkTile = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding(BaseModel):
    id: UUID
    name: str
    artwork: Artwork1

class Item(BaseModel):
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

class Pagination(BaseModel):
    current_offset: int
    total_count: int

class SeriesGroupingMetadata(BaseModel):
    series_grouping_type: str
    season_number: int
    grouping_name: str = Field(..., alias='groupingName')
    unknown: bool

class SeasonModel(BaseModel):
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
