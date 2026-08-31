from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from typing import Any
from uuid import UUID

class Query(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entity: str
    id: str

class LatestSeason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has_upcoming_season: bool = Field(..., alias='hasUpcomingSeason')
    has_last_ep_premiered: bool = Field(..., alias='hasLastEpPremiered')

class HasBotifyPageWorkerEnabled(BaseModel):
    model_config = ConfigDict(defer_build=True)
    disabled_paths: list[str] = Field(..., alias='disabledPaths')
    enabled: bool

class FeatureFlags(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has404_carousel_enabled: bool = Field(..., alias='has404CarouselEnabled')
    has_connected_auth_enabled: bool = Field(..., alias='hasConnectedAuthEnabled')
    has_unified_login_enabled: bool = Field(..., alias='hasUnifiedLoginEnabled')
    has_edna_login_on_pwa_enabled: bool = Field(..., alias='hasEdnaLoginOnPWAEnabled')
    has_edna_login_review_and_accept_enabled: bool = Field(..., alias='hasEdnaLoginReviewAndAcceptEnabled')
    has_updated_gender_options: bool = Field(..., alias='hasUpdatedGenderOptions')
    has_one_trust_script_enabled: bool = Field(..., alias='hasOneTrustScriptEnabled')
    has_one_trust_consent_sync_enabled: bool = Field(..., alias='hasOneTrustConsentSyncEnabled')
    has_one_trust_footer_change_activated: bool = Field(..., alias='hasOneTrustFooterChangeActivated')
    has_privacy_consent_package_enabled: bool = Field(..., alias='hasPrivacyConsentPackageEnabled')
    has_subscriber_agreement_update_enabled: bool = Field(..., alias='hasSubscriberAgreementUpdateEnabled')
    has_hulu_client_signup_age_limit_enabled: bool = Field(..., alias='hasHuluClientSignupAgeLimitEnabled')
    has_botify_page_worker_enabled: HasBotifyPageWorkerEnabled = Field(..., alias='hasBotifyPageWorkerEnabled')

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    title: str
    modal_id: str | None = Field(None, alias='modalId')

class Section(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section: str
    items: list[list[Item]]

class Modal(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    id: str
    css_class: str
    closable: bool
    body: str
    footer: str

class BigFooterItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sections: list[Section]
    modals: list[Modal]

class Item1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    href: str

class Component(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    style: None = Field(None)
    sticky_mode: bool | None = None
    cta_always: bool | None = None
    enable_cta_toaster: bool | None = None
    enable_minimal_nav: bool | None = Field(None, alias='enableMinimalNav')
    items: list[Item1] | None = None
    cta: None = Field(None)
    cta_hype_program: str | None = Field(None, alias='ctaHypeProgram')
    cta_button_style: str | None = None
    disable_logo: None = Field(None)
    signup_flow_entry: str | None = None
    cta_download_app_text: None = Field(None, alias='ctaDownloadAppText')
    welcome_options: str | None = Field(None, alias='welcomeOptions')
    enable_sticky_mode_always: bool | None = Field(None, alias='enableStickyModeAlways')
    metrics: dict[str, Any]
    id: str | None = None
    title: str | None = None
    description: str | None = None
    view_all_url: None = Field(None, alias='viewAllUrl')
    url_format: None = Field(None, alias='urlFormat')

class Artwork(BaseModel):
    model_config = ConfigDict(defer_build=True)
    horizontal_program_tile: None = Field(..., alias='horizontalProgramTile')
    vertical_hero: None = Field(..., alias='verticalHero')

class DetailEntity(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: None
    id: None
    name: None
    description: None
    network: None
    premiere_date: None = Field(..., alias='premiereDate')
    artwork: Artwork
    href: str
    require_live_package: bool = Field(..., alias='requireLivePackage')
    redirect_to: None = Field(..., alias='redirectTo')
    latest_season: dict[str, Any] = Field(..., alias='latestSeason')
    credits: None

class Metrics(BaseModel):
    model_config = ConfigDict(defer_build=True)
    collection_count: int = Field(..., alias='collectionCount')

class CartAbandonmentCopy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    plan_and_name_copy: None = Field(..., alias='planAndNameCopy')
    name_copy: None = Field(..., alias='nameCopy')
    plan_copy: None = Field(..., alias='planCopy')
    default_copy: None = Field(..., alias='defaultCopy')
    href: None

class ContentOverrides(BaseModel):
    model_config = ConfigDict(defer_build=True)
    override_name: None = Field(..., alias='overrideName')
    override_description: None = Field(..., alias='overrideDescription')

class Options(BaseModel):
    model_config = ConfigDict(defer_build=True)
    enable_brand: bool = Field(..., alias='enableBrand')
    enable_hotjar: bool = Field(..., alias='enableHotjar')
    enable_coppa_mode: bool = Field(..., alias='enableCOPPAMode')
    cta_mobile_flag: bool = Field(..., alias='ctaMobileFlag')
    cta_anon_copy: None = Field(..., alias='ctaAnonCopy')
    cta_anon_link: str = Field(..., alias='ctaAnonLink')
    cta_all_copy: None = Field(..., alias='ctaAllCopy')
    cta_all_link: None = Field(..., alias='ctaAllLink')
    cta_some_copy: None = Field(..., alias='ctaSomeCopy')
    cta_some_link: None = Field(..., alias='ctaSomeLink')
    cta_some_not_to_addon_copy: None = Field(..., alias='ctaSomeNotToAddonCopy')
    cta_some_not_to_addon_link: None = Field(..., alias='ctaSomeNotToAddonLink')
    cta_some_and_not_enrolled_copy: None = Field(..., alias='ctaSomeAndNotEnrolledCopy')
    cta_some_and_not_enrolled_link: None = Field(..., alias='ctaSomeAndNotEnrolledLink')
    cta_ineligible_copy: None = Field(..., alias='ctaIneligibleCopy')
    cta_ineligible_link: None = Field(..., alias='ctaIneligibleLink')
    cta_inactive_copy: None = Field(..., alias='ctaInactiveCopy')
    cta_inactive_link: None = Field(..., alias='ctaInactiveLink')
    cta_apple_copy: None = Field(..., alias='ctaAppleCopy')
    cta_apple_link: None = Field(..., alias='ctaAppleLink')
    cart_abandonment_copy: CartAbandonmentCopy = Field(..., alias='cartAbandonmentCopy')
    disable_footer: None = Field(..., alias='disableFooter')
    display_theme: None = Field(..., alias='displayTheme')
    page_type: str = Field(..., alias='pageType')
    allow_subscriber_traffic: bool = Field(..., alias='allowSubscriberTraffic')
    should_check_for_prepaid: bool = Field(..., alias='shouldCheckForPrepaid')
    cohort_check: bool = Field(..., alias='cohortCheck')
    check_program_window: bool = Field(..., alias='checkProgramWindow')
    footer: None
    content_overrides: ContentOverrides = Field(..., alias='contentOverrides')

class Program(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partner: None
    hiswitch_packages: None = Field(..., alias='hiswitchPackages')
    type: None
    require_device_code: None = Field(..., alias='requireDeviceCode')

class Metatag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: str
    value_name: str = Field(..., alias='valueName')
    key_name: str = Field(..., alias='keyName')
    tag: str
    key: str

class Layout(BaseModel):
    model_config = ConfigDict(defer_build=True)
    locale: str
    big_footer: list[BigFooterItem] = Field(..., alias='bigFooter')
    bundle: None
    components: list[Component]
    detail_entity: DetailEntity = Field(..., alias='detailEntity')
    metrics: Metrics
    options: Options
    program: Program
    require_live_package: bool = Field(..., alias='requireLivePackage')
    redirect_to: None = Field(..., alias='redirectTo')
    metatags: list[Metatag]
    title: str

class Geodata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    geodata_overrides: dict[str, Any] = Field(..., alias='geodataOverrides')

class User(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_hulu_user: bool = Field(..., alias='isHuluUser')
    is_subscriber: bool = Field(..., alias='isSubscriber')
    entitlement_state: int = Field(..., alias='entitlementState')
    entitlement_flag: bool = Field(..., alias='entitlementFlag')
    is_apple_billed: bool = Field(..., alias='isAppleBilled')
    name: str

class DatadogRum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    application_id: UUID = Field(..., alias='applicationId')
    client_token: str = Field(..., alias='clientToken')

class Endpoints(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signup: str
    hoth: str
    hudis: str
    site: str
    home: str
    hookup: str
    user_model: str
    midgard: str
    acp: str
    edge: str

class Keys(BaseModel):
    model_config = ConfigDict(defer_build=True)
    facebook_app_id: str

class OneTrust(BaseModel):
    model_config = ConfigDict(defer_build=True)
    guuid: UUID
    sdk_url: str = Field(..., alias='sdkUrl')

class Config(BaseModel):
    model_config = ConfigDict(defer_build=True)
    app_component_name: str = Field(..., alias='appComponentName')
    ga_env: str = Field(..., alias='gaEnv')
    tealium_env: str = Field(..., alias='tealiumEnv')
    disable_recaptcha: bool = Field(..., alias='disableRecaptcha')
    login_modal_env: str = Field(..., alias='loginModalEnv')
    web_login_env: str = Field(..., alias='webLoginEnv')
    datadog_rum: DatadogRum = Field(..., alias='datadogRum')
    endpoints: Endpoints
    keys: Keys
    one_trust: OneTrust = Field(..., alias='oneTrust')
    hulu_env: str = Field(..., alias='huluEnv')

class PageProps(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_title: str = Field(..., alias='pageTitle')
    as_path: str = Field(..., alias='asPath')
    page_type: str = Field(..., alias='pageType')
    query: Query
    host: str
    latest_season: LatestSeason = Field(..., alias='latestSeason')
    feature_flags: FeatureFlags = Field(..., alias='featureFlags')
    layout: Layout
    geodata: Geodata
    cart_abandonment: None = Field(..., alias='cartAbandonment')
    is_suf_returning_customer: bool = Field(..., alias='isSufReturningCustomer')
    use_analytics: bool = Field(..., alias='useAnalytics')
    collection_count: int = Field(..., alias='collectionCount')
    is_hiswitch: None = Field(..., alias='isHiswitch')
    user_is_logged_in: bool = Field(..., alias='userIsLoggedIn')
    user_is_subscriber: bool = Field(..., alias='userIsSubscriber')
    user_is_age_eligible_for_advertising: bool = Field(..., alias='userIsAgeEligibleForAdvertising')
    user: User
    config: Config

class Props(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_props: PageProps = Field(..., alias='pageProps')

class RuntimeConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    app_component_name: str = Field(..., alias='appComponentName')
    ga_env: str = Field(..., alias='gaEnv')
    tealium_env: str = Field(..., alias='tealiumEnv')
    disable_recaptcha: bool = Field(..., alias='disableRecaptcha')
    login_modal_env: str = Field(..., alias='loginModalEnv')
    web_login_env: str = Field(..., alias='webLoginEnv')
    datadog_rum: DatadogRum = Field(..., alias='datadogRum')
    endpoints: Endpoints
    keys: Keys
    one_trust: OneTrust = Field(..., alias='oneTrust')
    hulu_env: str = Field(..., alias='huluEnv')

class GenreModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    props: Props
    page: str
    query: Query
    build_id: str = Field(..., alias='buildId')
    asset_prefix: str = Field(..., alias='assetPrefix')
    runtime_config: RuntimeConfig = Field(..., alias='runtimeConfig')
    is_fallback: bool = Field(..., alias='isFallback')
    custom_server: bool = Field(..., alias='customServer')
    gip: bool
    app_gip: bool = Field(..., alias='appGip')
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
