from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID
from typing import Any

class Accent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hue: int | None = None
    classification: str | None = None

class VideoHorizontalHero(BaseModel):
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

class VideoVerticalHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_horizontal_hero: VideoHorizontalHero | None = Field(None, alias='video.horizontal.hero')
    program_tile: ProgramTile | None = Field(None, alias='program.tile')
    video_vertical_hero: VideoVerticalHero | None = Field(None, alias='video.vertical.hero')

class ExternalIdentifier(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    namespace: str | None = None
    id: UUID | str | None = Field(default=None, union_mode='left_to_right')

class MetricsInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    metrics_asset_name: str | None = None
    airing_type: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None

class Personalization(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eab: str | None = None

class Browse(BaseModel):
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

class BrandWatermark(BaseModel):
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

class NetworkTile(BaseModel):
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

class BrandWatermarkDark(BaseModel):
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

class ProgramVerticalTile(BaseModel):
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

class Artwork1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark | None = Field(None, alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo | None = Field(None, alias='brand.logo')
    network_tile: NetworkTile | None = Field(None, alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight | None = Field(None, alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight | None = Field(None, alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark | None = Field(None, alias='brand.watermark.dark')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile | None = Field(None, alias='program.vertical.tile')
    brand_hub_background: BrandHubBackground | None = Field(None, alias='brand.hub.background')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None
    artwork: Artwork1 | None = None

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None

class DetailVerticalHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal(BaseModel):
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

class ProgramVerticalTile1(BaseModel):
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

class VideoHorizontalHero1(BaseModel):
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

class SeriesArtwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_vertical_hero: DetailVerticalHero | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile2 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero | None = Field(None, alias='detail.horizontal.hero')
    video_horizontal_hero: VideoHorizontalHero1 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked | None = Field(None, alias='title.treatment.stacked')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    name: str | None = None
    description: str | None = None
    artwork: Artwork | None = None
    metrics_info: MetricsInfo | None = None
    personalization: Personalization | None = None
    device_context_failure: bool | None = None
    browse: Browse | None = None
    series_id: UUID | None = None
    series_name: str | None = None
    season: str | None = None
    bundle: Bundle | None = None
    number: str | None = None
    primary_branding: PrimaryBranding | None = None
    rating: Rating | None = None
    genre_names: list[str] | None = None
    premiere_date: AwareDatetime | None = None
    is_first_run: bool | None = None
    series_artwork: SeriesArtwork | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    actions: list[Any] | None = None
    duration: int | None = None
    season_short_display_name: str | None = None

class Pagination(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    current_offset: int | None = None
    total_count: int | None = None

class SeriesGroupingMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    series_grouping_type: str | None = None
    season_number: int | None = None
    grouping_name: str | None = Field(None, alias='groupingName')
    unknown: bool | None = None

class SeasonModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    href: str | None = None
    p13n_href: str | None = None
    name: str | None = None
    theme: str | None = None
    artwork: dict[str, Any] | None = None
    device_context_failure: bool | None = None
    items: list[Item] | None = None
    pagination: Pagination | None = None
    series_grouping_metadata: SeriesGroupingMetadata | None = None
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
