from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID
from typing import Any

class Accent(BaseModel):
    model_config = ConfigDict(extra='ignore')
    hue: int | None = None
    classification: str | None = None

class DetailVerticalHero(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class VideoHorizontalHero(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore')
    detail_vertical_hero: DetailVerticalHero | None = Field(None, alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero | None = Field(None, alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero | None = Field(None, alias='detail.horizontal.hero')

class MetricsInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    page_type: str | None = None

class Browse(BaseModel):
    model_config = ConfigDict(extra='ignore')
    target_type: str | None = None
    target_id: UUID | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    type: str | None = None

class Personalization(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bowie_context: str | None = None

class DetailVerticalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class VideoHorizontalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    detail_vertical_hero: DetailVerticalHero1 | None = Field(None, alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero1 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal1 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile1 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile1 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero1 | None = Field(None, alias='detail.horizontal.hero')

class ExternalIdentifier(BaseModel):
    model_config = ConfigDict(extra='ignore')
    namespace: str | None = None
    id: str | None = None

class MetricsInfo1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    reco_tags: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None
    selection_tracking_id: UUID | None = None
    metrics_asset_name: str | None = None
    airing_type: str | None = None

class Personalization1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    eab: str | None = None

class Browse1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    target_type: str | None = None
    target_id: UUID | None = None
    target_theme: str | None = None
    params: dict[str, Any] | None = None
    href: str | None = None
    browse_theme: str | None = None
    type: str | None = None

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore')
    code: str | None = None

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    start_date: AwareDatetime | None = None
    end_date: AwareDatetime | None = None
    location_requirement: str | None = None
    is_available: bool | None = None

class Rights(BaseModel):
    model_config = ConfigDict(extra='ignore')
    startover: bool | None = None
    recordable: bool | None = None
    offline: bool | None = None
    client_override: bool | None = None
    co_viewing: bool | None = None

class Bundle(BaseModel):
    model_config = ConfigDict(extra='ignore')
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

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    name: str | None = None
    description: str | None = None
    artwork: Artwork1 | None = None
    metrics_info: MetricsInfo1 | None = None
    personalization: Personalization1 | None = None
    device_context_failure: bool | None = None
    browse: Browse1 | None = None
    genre_names: list[str] | None = None
    rating: Rating | None = None
    premiere_date: AwareDatetime | None = None
    duration: int | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    actions: list[Any] | None = None
    original_id: UUID | None = None
    original_type: str | None = None
    relationship: str | None = None
    bundle: Bundle | None = None

class Pagination(BaseModel):
    model_config = ConfigDict(extra='ignore')
    current_offset: int | None = None

class Component(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    href: str | None = None
    p13n_href: str | None = None
    name: str | None = None
    theme: str | None = None
    artwork: dict[str, Any] | None = None
    personalization: Personalization | None = None
    device_context_failure: bool | None = None
    items: list[Item] | None = None
    actions: list[Any] | None = None
    pagination: Pagination | None = None
    is_fallback: bool | None = None

class VideoHorizontalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_horizontal_hero: VideoHorizontalHero2 | None = Field(None, alias='video.horizontal.hero')

class MetricsInfo2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    metrics_asset_name: str | None = None
    airing_type: str | None = None

class Bundle1(BaseModel):
    model_config = ConfigDict(extra='ignore')
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

class Trailer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    name: str | None = None
    description: str | None = None
    artwork: Artwork2 | None = None
    metrics_info: MetricsInfo2 | None = None
    device_context_failure: bool | None = None
    browse: Browse1 | None = None
    genre_names: list[str] | None = None
    original_id: UUID | None = None
    original_type: str | None = None
    rating: Rating | None = None
    premiere_date: AwareDatetime | None = None
    relationship: str | None = None
    bundle: Bundle1 | None = None
    restriction_level: str | None = None
    actions: list[Any] | None = None

class DetailVerticalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class VideoHorizontalHero3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    detail_vertical_hero: DetailVerticalHero2 | None = Field(None, alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero3 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal2 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile2 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile2 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero2 | None = Field(None, alias='detail.horizontal.hero')

class MetricsInfo3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    metrics_asset_name: str | None = None
    airing_type: str | None = None
    external_identifiers: list[ExternalIdentifier] | None = None

class Bundle2(BaseModel):
    model_config = ConfigDict(extra='ignore')
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

class Entity(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    name: str | None = None
    description: str | None = None
    artwork: Artwork3 | None = None
    metrics_info: MetricsInfo3 | None = None
    personalization: Personalization1 | None = None
    device_context_failure: bool | None = None
    browse: Browse1 | None = None
    genre_names: list[str] | None = None
    bundle: Bundle2 | None = None
    rating: Rating | None = None
    premiere_date: AwareDatetime | None = None
    duration: int | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None

class MetricsInfo4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    reco_tags: str | None = None
    selection_tracking_id: UUID | None = None

class Focus(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    entity: Entity | None = None
    action_text: str | None = None
    metrics_info: MetricsInfo4 | None = None

class VodItems(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    focus: Focus | None = None

class UserState(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    is_warm: bool | None = None
    is_cold: bool | None = None

class DetailVerticalHero3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class VideoHorizontalHero4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class TitleTreatmentHorizontal3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramTile3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class ProgramVerticalTile3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class DetailHorizontalHero3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    accent: Accent | None = None
    image_type: str | None = None
    image_id: str | None = None

class Artwork4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    detail_vertical_hero: DetailVerticalHero3 | None = Field(None, alias='detail.vertical.hero')
    video_horizontal_hero: VideoHorizontalHero4 | None = Field(None, alias='video.horizontal.hero')
    title_treatment_horizontal: TitleTreatmentHorizontal3 | None = Field(None, alias='title.treatment.horizontal')
    program_tile: ProgramTile3 | None = Field(None, alias='program.tile')
    program_vertical_tile: ProgramVerticalTile3 | None = Field(None, alias='program.vertical.tile')
    detail_horizontal_hero: DetailHorizontalHero3 | None = Field(None, alias='detail.horizontal.hero')

class MetricsInfo5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    external_identifiers: list[ExternalIdentifier] | None = None

class Entity1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    id: UUID | None = None
    href: str | None = None
    p13n_href: str | None = None
    name: str | None = None
    description: str | None = None
    artwork: Artwork4 | None = None
    metrics_info: MetricsInfo5 | None = None
    personalization: Personalization1 | None = None
    device_context_failure: bool | None = None
    browse: Browse1 | None = None
    genre_names: list[str] | None = None
    rating: Rating | None = None
    premiere_date: AwareDatetime | None = None
    duration: int | None = None
    restriction_level: str | None = None
    exclusivity: str | None = None
    actions: list[Any] | None = None

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display_text: str | None = None

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore')
    prefix: str | None = None
    items: list[Item1] | None = None

class Details(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='_type')
    trailer: Trailer | None = None
    vod_items: VodItems | None = None
    user_state: UserState | None = None
    entity: Entity1 | None = None
    credits: list[Credit] | None = None

class MoviesModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
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
