from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID
from typing import Any

class Accent(BaseModel):
    hue: int
    classification: str

class DetailVerticalHero(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero(BaseModel):
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

class Artwork(BaseModel):
    detail_vertical_hero: DetailVerticalHero = Field(..., alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero = Field(..., alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile = Field(..., alias='program.tile')
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

class Personalization(BaseModel):
    bowie_context: str

class DetailVerticalHero1(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero1(BaseModel):
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

class Artwork1(BaseModel):
    detail_vertical_hero: DetailVerticalHero1 | None = Field(None, alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero1 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero1 | None = Field(None, alias='detail.horizontal.hero')

class ExternalIdentifier(BaseModel):
    namespace: str
    id: str

class MetricsInfo1(BaseModel):
    field_type: str = Field(..., alias='_type')
    reco_tags: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None
    selection_tracking_id: UUID | None = None
    metrics_asset_name: str | None = None
    airing_type: str | None = None

class Personalization1(BaseModel):
    eab: str

class Browse1(BaseModel):
    target_type: str
    target_id: UUID
    target_theme: str
    params: dict[str, Any]
    href: str
    browse_theme: str
    type: str

class Rating(BaseModel):
    code: str

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

class Item(BaseModel):
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

class Pagination(BaseModel):
    current_offset: int

class Component(BaseModel):
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

class VideoHorizontalHero2(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class Artwork2(BaseModel):
    video_horizontal_hero: VideoHorizontalHero2 = Field(..., alias='video.horizontal.hero')

class MetricsInfo2(BaseModel):
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str

class Bundle1(BaseModel):
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

class Trailer(BaseModel):
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

class DetailVerticalHero2(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero3(BaseModel):
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

class Artwork3(BaseModel):
    detail_vertical_hero: DetailVerticalHero2 = Field(..., alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero3 = Field(..., alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal2 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile2 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile2 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero2 = Field(..., alias='detail.horizontal.hero')

class MetricsInfo3(BaseModel):
    field_type: str = Field(..., alias='_type')
    metrics_asset_name: str
    airing_type: str
    external_identifiers: list[ExternalIdentifier]

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

class Entity(BaseModel):
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
    focus: Focus

class UserState(BaseModel):
    field_type: str = Field(..., alias='_type')
    is_warm: bool
    is_cold: bool

class DetailVerticalHero3(BaseModel):
    path: str
    accent: Accent
    image_type: str
    image_id: str

class VideoHorizontalHero4(BaseModel):
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

class Artwork4(BaseModel):
    detail_vertical_hero: DetailVerticalHero3 = Field(..., alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero4 = Field(..., alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal3 = Field(..., alias='title.treatment.horizontal')
    program_tile: ProgramTile3 = Field(..., alias='program.tile')
    program_vertical_tile: ProgramVerticalTile3 = Field(..., alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero3 = Field(..., alias='detail.horizontal.hero')

class MetricsInfo5(BaseModel):
    field_type: str = Field(..., alias='_type')
    external_identifiers: list[ExternalIdentifier]

class Entity1(BaseModel):
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

class Item1(BaseModel):
    display_text: str

class Credit(BaseModel):
    prefix: str
    items: list[Item1]

class Details(BaseModel):
    field_type: str = Field(..., alias='_type')
    trailer: Trailer
    vod_items: VodItems
    user_state: UserState
    entity: Entity1
    credits: list[Credit]

class MoviesModel(BaseModel):
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
