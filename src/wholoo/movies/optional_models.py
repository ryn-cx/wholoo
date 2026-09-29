from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID
from typing import Any

class Accent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hue: int | Any = Field(default=None, union_mode='left_to_right')
    classification: str | Any = Field(default=None, union_mode='left_to_right')

class TitleTreatmentHorizontal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramTile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class DetailVerticalHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramVerticalTile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class DetailHorizontalHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class VideoHorizontalHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class TitleTreatmentStacked(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_treatment_horizontal: TitleTreatmentHorizontal | Any = Field(None, alias='title.treatment.horizontal', union_mode='left_to_right')
    program_tile: ProgramTile | Any = Field(None, alias='program.tile', union_mode='left_to_right')
    detail_vertical_hero: DetailVerticalHero | Any = Field(None, alias='detail.vertical.hero', union_mode='left_to_right')
    program_vertical_tile: ProgramVerticalTile | Any = Field(None, alias='program.vertical.tile', union_mode='left_to_right')
    detail_horizontal_hero: DetailHorizontalHero | Any = Field(None, alias='detail.horizontal.hero', union_mode='left_to_right')
    video_horizontal_hero: VideoHorizontalHero | Any = Field(None, alias='video.horizontal.hero', union_mode='left_to_right')
    title_treatment_stacked: TitleTreatmentStacked | Any = Field(None, alias='title.treatment.stacked', union_mode='left_to_right')

class MetricsInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    page_type: str | Any = Field(default=None, union_mode='left_to_right')

class Browse(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    target_theme: str | Any = Field(default=None, union_mode='left_to_right')
    params: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Personalization(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bowie_context: str | Any = Field(default=None, union_mode='left_to_right')

class DetailVerticalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class TitleTreatmentHorizontal1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramTile1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramVerticalTile1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class DetailHorizontalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class TitleTreatmentStacked1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class DetailHorizontalWide(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class VideoHorizontalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_vertical_hero: DetailVerticalHero1 | Any = Field(None, alias='detail.vertical.hero', union_mode='left_to_right')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | Any = Field(None, alias='title.treatment.horizontal', union_mode='left_to_right')
    program_tile: ProgramTile1 | Any = Field(None, alias='program.tile', union_mode='left_to_right')
    program_vertical_tile: ProgramVerticalTile1 | Any = Field(None, alias='program.vertical.tile', union_mode='left_to_right')
    detail_horizontal_hero: DetailHorizontalHero1 | Any = Field(None, alias='detail.horizontal.hero', union_mode='left_to_right')
    title_treatment_stacked: TitleTreatmentStacked1 | Any = Field(None, alias='title.treatment.stacked', union_mode='left_to_right')
    detail_horizontal_wide: DetailHorizontalWide | Any = Field(None, alias='detail.horizontal.wide', union_mode='left_to_right')
    video_horizontal_hero: VideoHorizontalHero1 | Any = Field(None, alias='video.horizontal.hero', union_mode='left_to_right')

class ExternalIdentifier(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    namespace: str | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | str | Any = Field(default=None, union_mode='left_to_right')

class MetricsInfo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    reco_tags: str | Any = Field(default=None, union_mode='left_to_right')
    selection_tracking_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    external_identifiers: list[ExternalIdentifier] | Any = Field(default=None, union_mode='left_to_right')
    metrics_asset_name: str | Any = Field(default=None, union_mode='left_to_right')
    airing_type: str | Any = Field(default=None, union_mode='left_to_right')

class Personalization1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eab: str | Any = Field(default=None, union_mode='left_to_right')

class Browse1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_type: str | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    target_theme: str | Any = Field(default=None, union_mode='left_to_right')
    params: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    browse_theme: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermark(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkTopRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class NetworkTile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkBottomRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoTopRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoBottomRight(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramTile2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramVerticalTile2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandHubBackground(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkDark(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark | Any = Field(None, alias='brand.watermark', union_mode='left_to_right')
    brand_watermark_top_right: BrandWatermarkTopRight | Any = Field(None, alias='brand.watermark.top.right', union_mode='left_to_right')
    brand_logo: BrandLogo | Any = Field(None, alias='brand.logo', union_mode='left_to_right')
    network_tile: NetworkTile | Any = Field(None, alias='network.tile', union_mode='left_to_right')
    brand_watermark_bottom_right: BrandWatermarkBottomRight | Any = Field(None, alias='brand.watermark.bottom.right', union_mode='left_to_right')
    brand_logo_top_right: BrandLogoTopRight | Any = Field(None, alias='brand.logo.top.right', union_mode='left_to_right')
    brand_logo_bottom_right: BrandLogoBottomRight | Any = Field(None, alias='brand.logo.bottom.right', union_mode='left_to_right')
    program_tile: ProgramTile2 | Any = Field(None, alias='program.tile', union_mode='left_to_right')
    program_vertical_tile: ProgramVerticalTile2 | Any = Field(None, alias='program.vertical.tile', union_mode='left_to_right')
    brand_hub_background: BrandHubBackground | Any = Field(None, alias='brand.hub.background', union_mode='left_to_right')
    brand_watermark_dark: BrandWatermarkDark | Any = Field(None, alias='brand.watermark.dark', union_mode='left_to_right')

class PrimaryBranding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork2 | Any = Field(default=None, union_mode='left_to_right')

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    start_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    end_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    location_requirement: str | Any = Field(default=None, union_mode='left_to_right')
    is_available: bool | Any = Field(default=None, union_mode='left_to_right')

class Rights(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    startover: bool | Any = Field(default=None, union_mode='left_to_right')
    recordable: bool | Any = Field(default=None, union_mode='left_to_right')
    offline: bool | Any = Field(default=None, union_mode='left_to_right')
    client_override: bool | Any = Field(default=None, union_mode='left_to_right')
    co_viewing: bool | Any = Field(default=None, union_mode='left_to_right')

class Bundle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    eab_id: str | Any = Field(default=None, union_mode='left_to_right')
    network_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    network_name: str | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    availability: Availability | Any = Field(default=None, union_mode='left_to_right')
    bundle_type: str | Any = Field(default=None, union_mode='left_to_right')
    open_credit_end_pos: int | Any = Field(default=None, union_mode='left_to_right')
    close_credit_start_pos: int | Any = Field(default=None, union_mode='left_to_right')
    rights: Rights | Any = Field(default=None, union_mode='left_to_right')
    cp_id: int | Any = Field(default=None, union_mode='left_to_right')
    all_etag: str | Any = Field(default=None, union_mode='left_to_right')
    rights_etag: str | Any = Field(default=None, union_mode='left_to_right')
    airings_etag: str | Any = Field(default=None, union_mode='left_to_right')
    stream_etag: str | Any = Field(default=None, union_mode='left_to_right')
    rights_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    airings_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    stream_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(default=None, union_mode='left_to_right')
    av_features: list[str] | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork1 | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo1 | Any = Field(default=None, union_mode='left_to_right')
    personalization: Personalization1 | Any = Field(default=None, union_mode='left_to_right')
    device_context_failure: bool | Any = Field(default=None, union_mode='left_to_right')
    browse: Browse1 | Any = Field(default=None, union_mode='left_to_right')
    genre_names: list[str] | Any = Field(default=None, union_mode='left_to_right')
    episodes: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    rating: Rating | Any = Field(default=None, union_mode='left_to_right')
    premiere_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    restriction_level: str | Any = Field(default=None, union_mode='left_to_right')
    exclusivity: str | Any = Field(default=None, union_mode='left_to_right')
    is_rolling: bool | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    primary_branding: PrimaryBranding | Any = Field(default=None, union_mode='left_to_right')
    bundle: Bundle | Any = Field(default=None, union_mode='left_to_right')
    original_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    original_type: str | Any = Field(default=None, union_mode='left_to_right')
    relationship: str | Any = Field(default=None, union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    position: int | Any = Field(default=None, union_mode='left_to_right')

class Pagination(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    current_offset: int | Any = Field(default=None, union_mode='left_to_right')

class Component(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    p13n_href: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    theme: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
    personalization: Personalization | Any = Field(default=None, union_mode='left_to_right')
    device_context_failure: bool | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action] | Any = Field(default=None, union_mode='left_to_right')
    pagination: Pagination | Any = Field(default=None, union_mode='left_to_right')
    is_fallback: bool | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class DetailVerticalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class TitleTreatmentHorizontal2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramTile3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramVerticalTile3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class DetailHorizontalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class VideoHorizontalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class TitleTreatmentStacked2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_vertical_hero: DetailVerticalHero2 | Any = Field(None, alias='detail.vertical.hero', union_mode='left_to_right')
    title_treatment_horizontal: TitleTreatmentHorizontal2 | Any = Field(None, alias='title.treatment.horizontal', union_mode='left_to_right')
    program_tile: ProgramTile3 | Any = Field(None, alias='program.tile', union_mode='left_to_right')
    program_vertical_tile: ProgramVerticalTile3 | Any = Field(None, alias='program.vertical.tile', union_mode='left_to_right')
    detail_horizontal_hero: DetailHorizontalHero2 | Any = Field(None, alias='detail.horizontal.hero', union_mode='left_to_right')
    video_horizontal_hero: VideoHorizontalHero2 | Any = Field(None, alias='video.horizontal.hero', union_mode='left_to_right')
    title_treatment_stacked: TitleTreatmentStacked2 | Any = Field(None, alias='title.treatment.stacked', union_mode='left_to_right')

class MetricsInfo2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    metrics_asset_name: str | Any = Field(default=None, union_mode='left_to_right')
    airing_type: str | Any = Field(default=None, union_mode='left_to_right')
    external_identifiers: list[ExternalIdentifier] | Any = Field(default=None, union_mode='left_to_right')

class Bundle1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    eab_id: str | Any = Field(default=None, union_mode='left_to_right')
    network_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    network_name: str | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    availability: Availability | Any = Field(default=None, union_mode='left_to_right')
    bundle_type: str | Any = Field(default=None, union_mode='left_to_right')
    open_credit_end_pos: int | Any = Field(default=None, union_mode='left_to_right')
    close_credit_start_pos: int | Any = Field(default=None, union_mode='left_to_right')
    rights: Rights | Any = Field(default=None, union_mode='left_to_right')
    cp_id: int | Any = Field(default=None, union_mode='left_to_right')
    all_etag: str | Any = Field(default=None, union_mode='left_to_right')
    rights_etag: str | Any = Field(default=None, union_mode='left_to_right')
    airings_etag: str | Any = Field(default=None, union_mode='left_to_right')
    stream_etag: str | Any = Field(default=None, union_mode='left_to_right')
    rights_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    airings_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    stream_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(default=None, union_mode='left_to_right')
    av_features: list[str] | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermark1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkTopRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class NetworkTile1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkBottomRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoTopRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoBottomRight1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramTile4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramVerticalTile4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandHubBackground1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark1 | Any = Field(None, alias='brand.watermark', union_mode='left_to_right')
    brand_watermark_top_right: BrandWatermarkTopRight1 | Any = Field(None, alias='brand.watermark.top.right', union_mode='left_to_right')
    brand_logo: BrandLogo1 | Any = Field(None, alias='brand.logo', union_mode='left_to_right')
    network_tile: NetworkTile1 | Any = Field(None, alias='network.tile', union_mode='left_to_right')
    brand_watermark_bottom_right: BrandWatermarkBottomRight1 | Any = Field(None, alias='brand.watermark.bottom.right', union_mode='left_to_right')
    brand_logo_top_right: BrandLogoTopRight1 | Any = Field(None, alias='brand.logo.top.right', union_mode='left_to_right')
    brand_logo_bottom_right: BrandLogoBottomRight1 | Any = Field(None, alias='brand.logo.bottom.right', union_mode='left_to_right')
    program_tile: ProgramTile4 | Any = Field(None, alias='program.tile', union_mode='left_to_right')
    program_vertical_tile: ProgramVerticalTile4 | Any = Field(None, alias='program.vertical.tile', union_mode='left_to_right')
    brand_hub_background: BrandHubBackground1 | Any = Field(None, alias='brand.hub.background', union_mode='left_to_right')

class PrimaryBranding1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork4 | Any = Field(default=None, union_mode='left_to_right')

class Entity(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork3 | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo2 | Any = Field(default=None, union_mode='left_to_right')
    personalization: Personalization1 | Any = Field(default=None, union_mode='left_to_right')
    device_context_failure: bool | Any = Field(default=None, union_mode='left_to_right')
    browse: Browse1 | Any = Field(default=None, union_mode='left_to_right')
    genre_names: list[str] | Any = Field(default=None, union_mode='left_to_right')
    bundle: Bundle1 | Any = Field(default=None, union_mode='left_to_right')
    rating: Rating | Any = Field(default=None, union_mode='left_to_right')
    premiere_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    restriction_level: str | Any = Field(default=None, union_mode='left_to_right')
    exclusivity: str | Any = Field(default=None, union_mode='left_to_right')
    primary_branding: PrimaryBranding1 | Any = Field(default=None, union_mode='left_to_right')

class MetricsInfo3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    reco_tags: str | Any = Field(default=None, union_mode='left_to_right')
    selection_tracking_id: UUID | Any = Field(default=None, union_mode='left_to_right')

class Focus(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    entity: Entity | Any = Field(default=None, union_mode='left_to_right')
    action_text: str | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo3 | Any = Field(default=None, union_mode='left_to_right')

class VodItems(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    focus: Focus | Any = Field(default=None, union_mode='left_to_right')

class UserState(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    is_warm: bool | Any = Field(default=None, union_mode='left_to_right')
    is_cold: bool | Any = Field(default=None, union_mode='left_to_right')

class TitleTreatmentHorizontal3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramTile5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class DetailVerticalHero3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class ProgramVerticalTile5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class DetailHorizontalHero3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class VideoHorizontalHero3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class TitleTreatmentStacked3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_treatment_horizontal: TitleTreatmentHorizontal3 | Any = Field(None, alias='title.treatment.horizontal', union_mode='left_to_right')
    program_tile: ProgramTile5 | Any = Field(None, alias='program.tile', union_mode='left_to_right')
    detail_vertical_hero: DetailVerticalHero3 | Any = Field(None, alias='detail.vertical.hero', union_mode='left_to_right')
    program_vertical_tile: ProgramVerticalTile5 | Any = Field(None, alias='program.vertical.tile', union_mode='left_to_right')
    detail_horizontal_hero: DetailHorizontalHero3 | Any = Field(None, alias='detail.horizontal.hero', union_mode='left_to_right')
    video_horizontal_hero: VideoHorizontalHero3 | Any = Field(None, alias='video.horizontal.hero', union_mode='left_to_right')
    title_treatment_stacked: TitleTreatmentStacked3 | Any = Field(None, alias='title.treatment.stacked', union_mode='left_to_right')

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    external_identifiers: list[ExternalIdentifier] | Any = Field(default=None, union_mode='left_to_right')

class Entity1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    p13n_href: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork5 | Any = Field(default=None, union_mode='left_to_right')
    personalization: Personalization1 | Any = Field(default=None, union_mode='left_to_right')
    device_context_failure: bool | Any = Field(default=None, union_mode='left_to_right')
    browse: Browse1 | Any = Field(default=None, union_mode='left_to_right')
    genre_names: list[str] | Any = Field(default=None, union_mode='left_to_right')
    rating: Rating | Any = Field(default=None, union_mode='left_to_right')
    premiere_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    restriction_level: str | Any = Field(default=None, union_mode='left_to_right')
    exclusivity: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo4 | Any = Field(default=None, union_mode='left_to_right')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_text: str | Any = Field(default=None, union_mode='left_to_right')

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    prefix: str | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item1] | Any = Field(default=None, union_mode='left_to_right')

class VideoHorizontalHero4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_horizontal_hero: VideoHorizontalHero4 | Any = Field(None, alias='video.horizontal.hero', union_mode='left_to_right')

class MetricsInfo5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    metrics_asset_name: str | Any = Field(default=None, union_mode='left_to_right')
    airing_type: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermark2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkTopRight2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogo2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class NetworkTile2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandWatermarkBottomRight2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoTopRight2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoBottomRight2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    accent: Accent | Any = Field(default=None, union_mode='left_to_right')
    image_type: str | Any = Field(default=None, union_mode='left_to_right')
    image_id: str | Any = Field(default=None, union_mode='left_to_right')

class Artwork7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_watermark: BrandWatermark2 | Any = Field(None, alias='brand.watermark', union_mode='left_to_right')
    brand_watermark_top_right: BrandWatermarkTopRight2 | Any = Field(None, alias='brand.watermark.top.right', union_mode='left_to_right')
    brand_logo: BrandLogo2 | Any = Field(None, alias='brand.logo', union_mode='left_to_right')
    network_tile: NetworkTile2 | Any = Field(None, alias='network.tile', union_mode='left_to_right')
    brand_watermark_bottom_right: BrandWatermarkBottomRight2 | Any = Field(None, alias='brand.watermark.bottom.right', union_mode='left_to_right')
    brand_logo_top_right: BrandLogoTopRight2 | Any = Field(None, alias='brand.logo.top.right', union_mode='left_to_right')
    brand_logo_bottom_right: BrandLogoBottomRight2 | Any = Field(None, alias='brand.logo.bottom.right', union_mode='left_to_right')

class PrimaryBranding2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork7 | Any = Field(default=None, union_mode='left_to_right')

class Availability2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    start_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    location_requirement: str | Any = Field(default=None, union_mode='left_to_right')
    is_available: bool | Any = Field(default=None, union_mode='left_to_right')
    end_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')

class Bundle2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    eab_id: str | Any = Field(default=None, union_mode='left_to_right')
    network_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    network_name: str | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    availability: Availability2 | Any = Field(default=None, union_mode='left_to_right')
    bundle_type: str | Any = Field(default=None, union_mode='left_to_right')
    open_credit_end_pos: int | Any = Field(default=None, union_mode='left_to_right')
    close_credit_start_pos: int | Any = Field(default=None, union_mode='left_to_right')
    rights: Rights | Any = Field(default=None, union_mode='left_to_right')
    cp_id: int | Any = Field(default=None, union_mode='left_to_right')
    all_etag: str | Any = Field(default=None, union_mode='left_to_right')
    rights_etag: str | Any = Field(default=None, union_mode='left_to_right')
    airings_etag: str | Any = Field(default=None, union_mode='left_to_right')
    stream_etag: str | Any = Field(default=None, union_mode='left_to_right')
    rights_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    airings_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    stream_ttl: int | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(default=None, union_mode='left_to_right')
    av_features: list[str] | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')

class Trailer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork6 | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo5 | Any = Field(default=None, union_mode='left_to_right')
    device_context_failure: bool | Any = Field(default=None, union_mode='left_to_right')
    browse: Browse1 | Any = Field(default=None, union_mode='left_to_right')
    genre_names: list[str] | Any = Field(default=None, union_mode='left_to_right')
    original_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    original_type: str | Any = Field(default=None, union_mode='left_to_right')
    primary_branding: PrimaryBranding2 | Any = Field(default=None, union_mode='left_to_right')
    rating: Rating | Any = Field(default=None, union_mode='left_to_right')
    premiere_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    relationship: str | Any = Field(default=None, union_mode='left_to_right')
    bundle: Bundle2 | Any = Field(default=None, union_mode='left_to_right')
    restriction_level: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class Details(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    vod_items: VodItems | Any = Field(default=None, union_mode='left_to_right')
    user_state: UserState | Any = Field(default=None, union_mode='left_to_right')
    entity: Entity1 | Any = Field(default=None, union_mode='left_to_right')
    credits: list[Credit] | Any = Field(default=None, union_mode='left_to_right')
    trailer: Trailer | Any = Field(default=None, union_mode='left_to_right')

class MoviesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='_type', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    theme: str | Any = Field(default=None, union_mode='left_to_right')
    artwork: Artwork | Any = Field(default=None, union_mode='left_to_right')
    metrics_info: MetricsInfo | Any = Field(default=None, union_mode='left_to_right')
    device_context_failure: bool | Any = Field(default=None, union_mode='left_to_right')
    browse: Browse | Any = Field(default=None, union_mode='left_to_right')
    components: list[Component] | Any = Field(default=None, union_mode='left_to_right')
    details: Details | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Any] | Any = Field(default=None, union_mode='left_to_right')
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
