from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class Query(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entity: str | None = None
    id: str | None = None

class LatestSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_upcoming_season: bool | None = Field(None, alias='hasUpcomingSeason')
    has_last_ep_premiered: bool | None = Field(None, alias='hasLastEpPremiered')

class HasBotifyPageWorkerEnabled(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    disabled_paths: list[str] | None = Field(None, alias='disabledPaths')
    enabled: bool | None = None

class FeatureFlags(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has404_carousel_enabled: bool | None = Field(None, alias='has404CarouselEnabled')
    has_connected_auth_enabled: bool | None = Field(None, alias='hasConnectedAuthEnabled')
    has_unified_login_enabled: bool | None = Field(None, alias='hasUnifiedLoginEnabled')
    has_edna_login_on_pwa_enabled: bool | None = Field(None, alias='hasEdnaLoginOnPWAEnabled')
    has_edna_login_review_and_accept_enabled: bool | None = Field(None, alias='hasEdnaLoginReviewAndAcceptEnabled')
    has_updated_gender_options: bool | None = Field(None, alias='hasUpdatedGenderOptions')
    has_one_trust_script_enabled: bool | None = Field(None, alias='hasOneTrustScriptEnabled')
    has_one_trust_consent_sync_enabled: bool | None = Field(None, alias='hasOneTrustConsentSyncEnabled')
    has_one_trust_footer_change_activated: bool | None = Field(None, alias='hasOneTrustFooterChangeActivated')
    has_privacy_consent_package_enabled: bool | None = Field(None, alias='hasPrivacyConsentPackageEnabled')
    has_subscriber_agreement_update_enabled: bool | None = Field(None, alias='hasSubscriberAgreementUpdateEnabled')
    has_hulu_client_signup_age_limit_enabled: bool | None = Field(None, alias='hasHuluClientSignupAgeLimitEnabled')
    has_botify_page_worker_enabled: HasBotifyPageWorkerEnabled | None = Field(None, alias='hasBotifyPageWorkerEnabled')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    title: str | None = None
    modal_id: str | None = Field(None, alias='modalId')

class Section(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section: str | None = None
    items: list[list[Item]] | None = None

class Modal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    id: str | None = None
    css_class: str | None = None
    closable: bool | None = None
    body: str | None = None
    footer: str | None = None

class BigFooterItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sections: list[Section] | None = None
    modals: list[Modal] | None = None

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    href: str | None = None

class Component(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    style: Any | None = None
    sticky_mode: bool | None = None
    cta_always: bool | None = None
    enable_cta_toaster: bool | None = None
    enable_minimal_nav: bool | None = Field(None, alias='enableMinimalNav')
    items: list[Item1] | None = None
    cta: Any | None = None
    cta_hype_program: str | None = Field(None, alias='ctaHypeProgram')
    cta_button_style: str | None = None
    disable_logo: Any | None = None
    signup_flow_entry: str | None = None
    cta_download_app_text: Any | None = Field(None, alias='ctaDownloadAppText')
    welcome_options: str | None = Field(None, alias='welcomeOptions')
    enable_sticky_mode_always: bool | None = Field(None, alias='enableStickyModeAlways')
    metrics: dict[str, Any] | None = None
    id: str | None = None
    title: str | None = None
    description: str | None = None
    view_all_url: Any | None = Field(None, alias='viewAllUrl')
    url_format: Any | None = Field(None, alias='urlFormat')

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    horizontal_program_tile: Any | None = Field(None, alias='horizontalProgramTile')
    vertical_hero: Any | None = Field(None, alias='verticalHero')

class DetailEntity(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: Any | None = None
    id: Any | None = None
    name: Any | None = None
    description: Any | None = None
    network: Any | None = None
    premiere_date: Any | None = Field(None, alias='premiereDate')
    artwork: Artwork | None = None
    href: str | None = None
    require_live_package: bool | None = Field(None, alias='requireLivePackage')
    redirect_to: Any | None = Field(None, alias='redirectTo')
    latest_season: dict[str, Any] | None = Field(None, alias='latestSeason')
    credits: Any | None = None

class Metrics(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_count: int | None = Field(None, alias='collectionCount')

class CartAbandonmentCopy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    plan_and_name_copy: Any | None = Field(None, alias='planAndNameCopy')
    name_copy: Any | None = Field(None, alias='nameCopy')
    plan_copy: Any | None = Field(None, alias='planCopy')
    default_copy: Any | None = Field(None, alias='defaultCopy')
    href: Any | None = None

class ContentOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    override_name: Any | None = Field(None, alias='overrideName')
    override_description: Any | None = Field(None, alias='overrideDescription')

class Options(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_brand: bool | None = Field(None, alias='enableBrand')
    enable_hotjar: bool | None = Field(None, alias='enableHotjar')
    enable_coppa_mode: bool | None = Field(None, alias='enableCOPPAMode')
    cta_mobile_flag: bool | None = Field(None, alias='ctaMobileFlag')
    cta_anon_copy: Any | None = Field(None, alias='ctaAnonCopy')
    cta_anon_link: str | None = Field(None, alias='ctaAnonLink')
    cta_all_copy: Any | None = Field(None, alias='ctaAllCopy')
    cta_all_link: Any | None = Field(None, alias='ctaAllLink')
    cta_some_copy: Any | None = Field(None, alias='ctaSomeCopy')
    cta_some_link: Any | None = Field(None, alias='ctaSomeLink')
    cta_some_not_to_addon_copy: Any | None = Field(None, alias='ctaSomeNotToAddonCopy')
    cta_some_not_to_addon_link: Any | None = Field(None, alias='ctaSomeNotToAddonLink')
    cta_some_and_not_enrolled_copy: Any | None = Field(None, alias='ctaSomeAndNotEnrolledCopy')
    cta_some_and_not_enrolled_link: Any | None = Field(None, alias='ctaSomeAndNotEnrolledLink')
    cta_ineligible_copy: Any | None = Field(None, alias='ctaIneligibleCopy')
    cta_ineligible_link: Any | None = Field(None, alias='ctaIneligibleLink')
    cta_inactive_copy: Any | None = Field(None, alias='ctaInactiveCopy')
    cta_inactive_link: Any | None = Field(None, alias='ctaInactiveLink')
    cta_apple_copy: Any | None = Field(None, alias='ctaAppleCopy')
    cta_apple_link: Any | None = Field(None, alias='ctaAppleLink')
    cart_abandonment_copy: CartAbandonmentCopy | None = Field(None, alias='cartAbandonmentCopy')
    disable_footer: Any | None = Field(None, alias='disableFooter')
    display_theme: Any | None = Field(None, alias='displayTheme')
    page_type: str | None = Field(None, alias='pageType')
    allow_subscriber_traffic: bool | None = Field(None, alias='allowSubscriberTraffic')
    should_check_for_prepaid: bool | None = Field(None, alias='shouldCheckForPrepaid')
    cohort_check: bool | None = Field(None, alias='cohortCheck')
    check_program_window: bool | None = Field(None, alias='checkProgramWindow')
    footer: Any | None = None
    content_overrides: ContentOverrides | None = Field(None, alias='contentOverrides')

class Program(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    partner: Any | None = None
    hiswitch_packages: Any | None = Field(None, alias='hiswitchPackages')
    type: Any | None = None
    require_device_code: Any | None = Field(None, alias='requireDeviceCode')

class Metatag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    value: str | None = None
    value_name: str | None = Field(None, alias='valueName')
    key_name: str | None = Field(None, alias='keyName')
    tag: str | None = None
    key: str | None = None

class Layout(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    locale: str | None = None
    big_footer: list[BigFooterItem] | None = Field(None, alias='bigFooter')
    bundle: Any | None = None
    components: list[Component] | None = None
    detail_entity: DetailEntity | None = Field(None, alias='detailEntity')
    metrics: Metrics | None = None
    options: Options | None = None
    program: Program | None = None
    require_live_package: bool | None = Field(None, alias='requireLivePackage')
    redirect_to: Any | None = Field(None, alias='redirectTo')
    metatags: list[Metatag] | None = None
    title: str | None = None

class Geodata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    geodata_overrides: dict[str, Any] | None = Field(None, alias='geodataOverrides')

class User(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_hulu_user: bool | None = Field(None, alias='isHuluUser')
    is_subscriber: bool | None = Field(None, alias='isSubscriber')
    entitlement_state: int | None = Field(None, alias='entitlementState')
    entitlement_flag: bool | None = Field(None, alias='entitlementFlag')
    is_apple_billed: bool | None = Field(None, alias='isAppleBilled')
    name: str | None = None

class DatadogRum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    application_id: UUID | None = Field(None, alias='applicationId')
    client_token: str | None = Field(None, alias='clientToken')

class Endpoints(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signup: str | None = None
    hoth: str | None = None
    hudis: str | None = None
    site: str | None = None
    home: str | None = None
    hookup: str | None = None
    user_model: str | None = None
    midgard: str | None = None
    acp: str | None = None
    edge: str | None = None

class Keys(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    facebook_app_id: str | None = None

class OneTrust(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    guuid: UUID | None = None
    sdk_url: str | None = Field(None, alias='sdkUrl')

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app_component_name: str | None = Field(None, alias='appComponentName')
    ga_env: str | None = Field(None, alias='gaEnv')
    tealium_env: str | None = Field(None, alias='tealiumEnv')
    disable_recaptcha: bool | None = Field(None, alias='disableRecaptcha')
    login_modal_env: str | None = Field(None, alias='loginModalEnv')
    web_login_env: str | None = Field(None, alias='webLoginEnv')
    datadog_rum: DatadogRum | None = Field(None, alias='datadogRum')
    endpoints: Endpoints | None = None
    keys: Keys | None = None
    one_trust: OneTrust | None = Field(None, alias='oneTrust')
    hulu_env: str | None = Field(None, alias='huluEnv')

class PageProps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_title: str | None = Field(None, alias='pageTitle')
    as_path: str | None = Field(None, alias='asPath')
    page_type: str | None = Field(None, alias='pageType')
    query: Query | None = None
    host: str | None = None
    latest_season: LatestSeason | None = Field(None, alias='latestSeason')
    feature_flags: FeatureFlags | None = Field(None, alias='featureFlags')
    layout: Layout | None = None
    geodata: Geodata | None = None
    cart_abandonment: Any | None = Field(None, alias='cartAbandonment')
    is_suf_returning_customer: bool | None = Field(None, alias='isSufReturningCustomer')
    use_analytics: bool | None = Field(None, alias='useAnalytics')
    collection_count: int | None = Field(None, alias='collectionCount')
    is_hiswitch: Any | None = Field(None, alias='isHiswitch')
    user_is_logged_in: bool | None = Field(None, alias='userIsLoggedIn')
    user_is_subscriber: bool | None = Field(None, alias='userIsSubscriber')
    user_is_age_eligible_for_advertising: bool | None = Field(None, alias='userIsAgeEligibleForAdvertising')
    user: User | None = None
    config: Config | None = None

class Props(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_props: PageProps | None = Field(None, alias='pageProps')

class RuntimeConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app_component_name: str | None = Field(None, alias='appComponentName')
    ga_env: str | None = Field(None, alias='gaEnv')
    tealium_env: str | None = Field(None, alias='tealiumEnv')
    disable_recaptcha: bool | None = Field(None, alias='disableRecaptcha')
    login_modal_env: str | None = Field(None, alias='loginModalEnv')
    web_login_env: str | None = Field(None, alias='webLoginEnv')
    datadog_rum: DatadogRum | None = Field(None, alias='datadogRum')
    endpoints: Endpoints | None = None
    keys: Keys | None = None
    one_trust: OneTrust | None = Field(None, alias='oneTrust')
    hulu_env: str | None = Field(None, alias='huluEnv')

class GenreModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    props: Props | None = None
    page: str | None = None
    query: Query | None = None
    build_id: str | None = Field(None, alias='buildId')
    asset_prefix: str | None = Field(None, alias='assetPrefix')
    runtime_config: RuntimeConfig | None = Field(None, alias='runtimeConfig')
    is_fallback: bool | None = Field(None, alias='isFallback')
    custom_server: bool | None = Field(None, alias='customServer')
    gip: bool | None = None
    app_gip: bool | None = Field(None, alias='appGip')
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
