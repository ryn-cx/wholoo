from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID
from typing import Any

class Accent(BaseModel):
    hue: int
    classification: str

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

class DetailVerticalHero(BaseModel):
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

class Artwork(BaseModel):
    title_treatment_horizontal: TitleTreatmentHorizontal = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile = Field(..., alias='program.tile')
    detail_vertical_hero: DetailVerticalHero = Field(..., alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero = Field(..., alias='detail.horizontal.hero')

class MetricsInfo(BaseModel):
    field_type: str = Field(..., alias='_type')
    page_type: str

class Browse(BaseModel):
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    type: str

class VideoHorizontalHero(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailVerticalHero1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentStacked(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork1(BaseModel):
    video_horizontal_hero: VideoHorizontalHero | None = Field(None, alias='video.horizontal.hero')
    detail_vertical_hero: DetailVerticalHero1 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero1 | None = Field(None, alias='detail.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked | None = Field(None, alias='title.treatment.stacked')

class VideoHorizontalHero1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork2(BaseModel):
    video_horizontal_hero: VideoHorizontalHero1 = Field(..., alias='video.horizontal.hero')

class ExternalIdentifier(BaseModel):
    namespace: str
    id: str

class MetricsInfo1(BaseModel):
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier]

class Personalization(BaseModel):
    eab: str

class Browse1(BaseModel):
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

class DetailVerticalHero2(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal2(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile2(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile2(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero2(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class SeriesArtwork(BaseModel):
    detail_vertical_hero: DetailVerticalHero2 = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal2 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile2 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile2 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero2 = Field(..., alias='detail.horizontal.hero')

class Item1(BaseModel):
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

class Pagination(BaseModel):
    current_offset: int
    total_count: int
    next: str | None = None

class SeriesGroupingMetadata(BaseModel):
    series_grouping_type: str
    season_number: int
    grouping_name: str = Field(..., alias='groupingName')
    unknown: bool

class MetricsInfo2(BaseModel):
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str | None = None
    airing_type: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None
    reco_tags: str | None = None
    selection_tracking_id: UUID | None = None

class Bundle1(BaseModel):
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

class DetailVerticalHero3(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal3(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile3(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile3(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero3(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class SeriesArtwork1(BaseModel):
    detail_vertical_hero: DetailVerticalHero3 = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal3 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile3 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile3 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero3 = Field(..., alias='detail.horizontal.hero')

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

class BrandWatermarkDark(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile4(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile4(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork3(BaseModel):
    brand_watermark: BrandWatermark | None = Field(None, alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo | None = Field(None, alias='brand.logo')
    network_tile: NetworkTile = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight | None = Field(None, alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark | None = Field(None, alias='brand.watermark.dark')
    program_tile: ProgramTile4 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile4 | None = Field(None, alias='program.vertical.tile')

class PrimaryBranding(BaseModel):
    id: UUID
    name: str
    artwork: Artwork3

class Item(BaseModel):
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

class Pagination1(BaseModel):
    current_offset: int

class FocusNavigation(BaseModel):
    collection_id: str
    entity_id: UUID

class Personalization2(BaseModel):
    bowie_context: str

class Component(BaseModel):
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

class VideoHorizontalHero2(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork4(BaseModel):
    video_horizontal_hero: VideoHorizontalHero2 = Field(..., alias='video.horizontal.hero')

class MetricsInfo3(BaseModel):
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier]

class Personalization3(BaseModel):
    eab: str

class Bundle2(BaseModel):
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

class DetailVerticalHero4(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class TitleTreatmentHorizontal4(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile5(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile5(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero4(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class SeriesArtwork2(BaseModel):
    detail_vertical_hero: DetailVerticalHero4 = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal4 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile5 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile5 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero4 = Field(..., alias='detail.horizontal.hero')

class Entity(BaseModel):
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

class MetricsInfo4(BaseModel):
    reco_tags: str
    selection_tracking_id: UUID

class Focus(BaseModel):
    field_type: str = Field(..., alias='_type')
    entity: Entity
    action_text: str
    metrics_info: MetricsInfo4

class VodItems(BaseModel):
    field_type: str = Field(..., alias='_type')
    id: str
    collection_id: int
    focus: Focus

class UserState(BaseModel):
    field_type: str = Field(..., alias='_type')
    is_warm: bool
    is_cold: bool

class TitleTreatmentHorizontal5(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramTile6(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailVerticalHero5(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class ProgramVerticalTile6(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class DetailHorizontalHero5(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork5(BaseModel):
    title_treatment_horizontal: TitleTreatmentHorizontal5 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile6 = Field(..., alias='program.tile')
    detail_vertical_hero: DetailVerticalHero5 = Field(..., alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile6 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero5 = Field(..., alias='detail.horizontal.hero')

class MetricsInfo5(BaseModel):
    field_type: str = Field(..., alias='_type')
    external_identifiers: list[ExternalIdentifier]

class BrandWatermark1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkTopRight1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogo1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class NetworkTile1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandWatermarkBottomRight1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoTopRight1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class BrandLogoBottomRight1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork6(BaseModel):
    brand_watermark: BrandWatermark1 = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight1 = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo1 = Field(..., alias='brand.logo')
    network_tile: NetworkTile1 = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight1 = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight1 = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding1(BaseModel):
    id: UUID
    name: str
    artwork: Artwork6

class Entity1(BaseModel):
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

class Item2(BaseModel):
    display_text: str

class Credit(BaseModel):
    prefix: str
    items: list[Item2]

class Details(BaseModel):
    field_type: str = Field(..., alias='_type')
    vod_items: VodItems
    user_state: UserState
    entity: Entity1
    credits: list[Credit]

class TVModel(BaseModel):
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
