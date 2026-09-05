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

class VideoHorizontalHero(BaseModel):
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

class Artwork(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_treatment_horizontal: TitleTreatmentHorizontal | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile = Field(..., alias='program.tile')
    detail_vertical_hero: DetailVerticalHero = Field(..., alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero = Field(..., alias='detail.horizontal.hero')
    video_horizontal_hero: VideoHorizontalHero | None = Field(None, alias='video.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked | None = Field(None, alias='title.treatment.stacked')

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

class Personalization(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bowie_context: str

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

class Artwork1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_vertical_hero: DetailVerticalHero1 | None = Field(None, alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero1 | None = Field(None, alias='detail.horizontal.hero')
    video_horizontal_hero: VideoHorizontalHero1 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked1 | None = Field(None, alias='title.treatment.stacked')

class ExternalIdentifier(BaseModel):
    model_config = ConfigDict(defer_build=True)
    namespace: str
    id: UUID | str = Field(union_mode='left_to_right')

class MetricsInfo1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    reco_tags: str | None = None
    selection_tracking_id: UUID | None = None
    external_identifiers: list[ExternalIdentifier] | None = None
    metrics_asset_name: str | None = None
    airing_type: str | None = None

class Personalization1(BaseModel):
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

class Rating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str | None = None

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

class BrandHubBackground(BaseModel):
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

class ProgramVerticalTile2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark | None = Field(None, alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight | None = Field(None, alias='brand.watermark.top.right')
    brand_logo: BrandLogo | None = Field(None, alias='brand.logo')
    network_tile: NetworkTile = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight | None = Field(None, alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight = Field(..., alias='brand.logo.bottom.right')
    brand_watermark_dark: BrandWatermarkDark | None = Field(None, alias='brand.watermark.dark')
    brand_hub_background: BrandHubBackground | None = Field(None, alias='brand.hub.background')
    program_tile: ProgramTile2 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile2 | None = Field(None, alias='program.vertical.tile')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork2

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    start_date: AwareDatetime
    end_date: AwareDatetime
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

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork1
    metrics_info: MetricsInfo1 | None = None
    personalization: Personalization1
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    episodes: list[None] | None = None
    rating: Rating
    premiere_date: AwareDatetime | None = None
    restriction_level: str
    exclusivity: str | None = None
    is_rolling: bool | None = None
    actions: list[None]
    duration: int | None = None
    primary_branding: PrimaryBranding | None = None
    bundle: Bundle | None = None
    original_id: UUID | None = None
    original_type: str | None = None
    relationship: str | None = None

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: str
    name: str
    position: int

class Pagination(BaseModel):
    model_config = ConfigDict(defer_build=True)
    current_offset: int

class Component(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    actions: list[Action]
    pagination: Pagination
    is_fallback: bool
    description: str | None = None

class DetailVerticalHero2(BaseModel):
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

class ProgramTile3(BaseModel):
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

class DetailHorizontalHero2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero2(BaseModel):
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

class Artwork3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_vertical_hero: DetailVerticalHero2 = Field(..., alias='detail.vertical.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal2 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile3 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile3 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero2 = Field(..., alias='detail.horizontal.hero')
    video_horizontal_hero: VideoHorizontalHero2 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked2 | None = Field(None, alias='title.treatment.stacked')

class ExternalIdentifier1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    namespace: str
    id: str

class MetricsInfo2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier1] | None = None

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

class ProgramTile4(BaseModel):
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

class BrandHubBackground1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark1 = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight1 = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo1 = Field(..., alias='brand.logo')
    network_tile: NetworkTile1 = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight1 = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight1 = Field(..., alias='brand.logo.bottom.right')
    program_tile: ProgramTile4 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile4 | None = Field(None, alias='program.vertical.tile')
    brand_hub_background: BrandHubBackground1 | None = Field(None, alias='brand.hub.background')

class PrimaryBranding1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork4

class Entity(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork3
    metrics_info: MetricsInfo2
    personalization: Personalization1
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    bundle: Bundle1
    rating: Rating
    premiere_date: AwareDatetime
    duration: int | None = None
    restriction_level: str
    exclusivity: str
    primary_branding: PrimaryBranding1 | None = None

class MetricsInfo3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    reco_tags: str
    selection_tracking_id: UUID

class Focus(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    entity: Entity
    action_text: str
    metrics_info: MetricsInfo3

class VodItems(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: str
    focus: Focus

class UserState(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    is_warm: bool
    is_cold: bool

class TitleTreatmentHorizontal3(BaseModel):
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

class DetailVerticalHero3(BaseModel):
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

class VideoHorizontalHero3(BaseModel):
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

class Artwork5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_treatment_horizontal: TitleTreatmentHorizontal3 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile5 = Field(..., alias='program.tile')
    detail_vertical_hero: DetailVerticalHero3 = Field(..., alias='detail.vertical.hero')
    program_vertical_tile: ProgramVerticalTile5 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero3 = Field(..., alias='detail.horizontal.hero')
    video_horizontal_hero: VideoHorizontalHero3 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_stacked: TitleTreatmentStacked3 | None = Field(None, alias='title.treatment.stacked')

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    external_identifiers: list[ExternalIdentifier1]

class Entity1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    p13n_href: str
    name: str
    description: str
    artwork: Artwork5
    personalization: Personalization1
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    rating: Rating
    premiere_date: AwareDatetime
    duration: int | None = None
    restriction_level: str
    exclusivity: str
    actions: list[None]
    metrics_info: MetricsInfo4 | None = None

class Item1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display_text: str

class Credit(BaseModel):
    model_config = ConfigDict(defer_build=True)
    prefix: str
    items: list[Item1]

class VideoHorizontalHero4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_horizontal_hero: VideoHorizontalHero4 = Field(..., alias='video.horizontal.hero')

class MetricsInfo5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str

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

class Artwork7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_watermark: BrandWatermark2 = Field(..., alias='brand.watermark')
    brand_watermark_top_right: BrandWatermarkTopRight2 = Field(..., alias='brand.watermark.top.right')
    brand_logo: BrandLogo2 = Field(..., alias='brand.logo')
    network_tile: NetworkTile2 = Field(..., alias='network.tile')
    brand_watermark_bottom_right: BrandWatermarkBottomRight2 = Field(..., alias='brand.watermark.bottom.right')
    brand_logo_top_right: BrandLogoTopRight2 = Field(..., alias='brand.logo.top.right')
    brand_logo_bottom_right: BrandLogoBottomRight2 = Field(..., alias='brand.logo.bottom.right')

class PrimaryBranding2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str
    artwork: Artwork7

class Trailer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: UUID
    href: str
    name: str
    description: str
    artwork: Artwork6
    metrics_info: MetricsInfo5
    device_context_failure: bool
    browse: Browse1
    genre_names: list[str]
    original_id: UUID
    original_type: str
    rating: Rating
    premiere_date: AwareDatetime
    relationship: str
    bundle: Bundle2
    restriction_level: str
    actions: list[None]
    primary_branding: PrimaryBranding2 | None = None

class Details(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    vod_items: VodItems | None = None
    user_state: UserState
    entity: Entity1
    credits: list[Credit]
    trailer: Trailer | None = None

class MoviesModel(BaseModel):
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
