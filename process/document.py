from enum import Enum
from typing import Optional, Union, Dict, List
from datetime import datetime
from uuid import UUID


class RoleID(Enum):
    THE_5_C32_F8_B0_C8_B30_B080713663_B = "5c32f8b0c8b30b080713663b"
    THE_5_C32_F8_B0_C8_B30_B080713663_C = "5c32f8b0c8b30b080713663c"
    THE_5_C32_F8_B0_C8_B30_B080713663_D = "5c32f8b0c8b30b080713663d"
    THE_5_C32_F8_B0_C8_B30_B080713663_E = "5c32f8b0c8b30b080713663e"
    THE_5_C32_F8_B0_C8_B30_B080713663_F = "5c32f8b0c8b30b080713663f"
    THE_5_C32_F8_B0_C8_B30_B0807136640 = "5c32f8b0c8b30b0807136640"


class Status(Enum):
    ACTIVE = "active"
    DRAFT = "draft"
    PUBLISHED = "published"
    SUBSCRIBED = "subscribed"


class TagID(Enum):
    THE_5_C32_FDA6_C8_B30_B080713677_D = "5c32fda6c8b30b080713677d"
    THE_5_C346585_C8_B30_B08071367_A2 = "5c346585c8b30b08071367a2"
    THE_5_C3_F2_E75_C8_B30_B0807136847 = "5c3f2e75c8b30b0807136847"
    THE_5_C4819_F9_C8_B30_B080713685_B = "5c4819f9c8b30b080713685b"
    THE_5_C580_C32_C8_B30_B08071368_A9 = "5c580c32c8b30b08071368a9"
    THE_5_C6_CEA6_CC8_B30_B08071368_D1 = "5c6cea6cc8b30b08071368d1"
    THE_5_CB9_C601_C8_B30_B0807136954 = "5cb9c601c8b30b0807136954"
    THE_5_D71_FA7_BF2_E096051_C068_E3_A = "5d71fa7bf2e096051c068e3a"
    THE_5_D79_DDC5_F2_E096051_C068_E49 = "5d79ddc5f2e096051c068e49"
    THE_5_E86_D7_E42_A274904_FE5_E4_BA4 = "5e86d7e42a274904fe5e4ba4"
    THE_5_EDDD8_B22_A274904_FE5_E4_C78 = "5eddd8b22a274904fe5e4c78"
    THE_60_B07_E1_E859_E7904_C595_FB9_E = "60b07e1e859e7904c595fb9e"
    THE_617253_BEBFBB6904_C3_D25023 = "617253bebfbb6904c3d25023"


class Visibility(Enum):
    PUBLIC = "public"


class Datum:
    key: Optional[str]
    first_request: Optional[int]
    last_request: Optional[int]
    lifetime: Optional[int]
    count: Optional[int]
    id: Union[int, None, str]
    name: Optional[str]
    version: Optional[str]
    current_version: Optional[str]
    lock_key: Optional[str]
    locked: Optional[int]
    acquired_at: Optional[datetime]
    released_at: Optional[datetime]
    post_id: Optional[str]
    mobiledoc: Optional[str]
    created_at_ts: Optional[int]
    created_at: Optional[datetime]
    object_type: Optional[str]
    action_type: Optional[str]
    object_id: None
    created_by: Optional[str]
    updated_at: Optional[datetime]
    updated_by: Optional[str]
    role_id: Optional[RoleID]
    permission_id: Optional[str]
    uuid: Optional[UUID]
    title: Optional[str]
    slug: Optional[str]
    html: Optional[str]
    comment_id: Optional[str]
    plaintext: Optional[str]
    feature_image: Optional[str]
    featured: Optional[int]
    page: Optional[int]
    status: Optional[Status]
    locale: None
    visibility: Optional[Visibility]
    meta_title: None
    meta_description: None
    author_id: Optional[int]
    published_at: Optional[datetime]
    published_by: Optional[int]
    custom_excerpt: Optional[str]
    codeinjection_head: Optional[str]
    codeinjection_foot: Optional[str]
    og_image: None
    og_title: None
    og_description: None
    twitter_image: None
    twitter_title: None
    twitter_description: None
    custom_template: None
    sort_order: Optional[int]
    tag_id: Optional[TagID]
    description: Optional[str]
    user_id: Optional[str]
    value: Optional[str]
    type: Optional[str]
    email: Optional[str]
    subscribed_url: Optional[str]
    subscribed_referrer: Optional[str]
    unsubscribed_url: None
    unsubscribed_at: None
    parent_id: None
    ghost_auth_access_token: None
    ghost_auth_id: None
    password: Optional[str]
    profile_image: Optional[str]
    cover_image: Optional[str]
    bio: Optional[str]
    website: None
    location: Optional[str]
    facebook: None
    twitter: None
    accessibility: Optional[str]
    tour: Optional[str]
    last_seen: Optional[datetime]

    def __init__(self, key: Optional[str], first_request: Optional[int], last_request: Optional[int], lifetime: Optional[int], count: Optional[int], id: Union[int, None, str], name: Optional[str], version: Optional[str], current_version: Optional[str], lock_key: Optional[str], locked: Optional[int], acquired_at: Optional[datetime], released_at: Optional[datetime], post_id: Optional[str], mobiledoc: Optional[str], created_at_ts: Optional[int], created_at: Optional[datetime], object_type: Optional[str], action_type: Optional[str], object_id: None, created_by: Optional[str], updated_at: Optional[datetime], updated_by: Optional[str], role_id: Optional[RoleID], permission_id: Optional[str], uuid: Optional[UUID], title: Optional[str], slug: Optional[str], html: Optional[str], comment_id: Optional[str], plaintext: Optional[str], feature_image: Optional[str], featured: Optional[int], page: Optional[int], status: Optional[Status], locale: None, visibility: Optional[Visibility], meta_title: None, meta_description: None, author_id: Optional[int], published_at: Optional[datetime], published_by: Optional[int], custom_excerpt: Optional[str], codeinjection_head: Optional[str], codeinjection_foot: Optional[str], og_image: None, og_title: None, og_description: None, twitter_image: None, twitter_title: None, twitter_description: None, custom_template: None, sort_order: Optional[int], tag_id: Optional[TagID], description: Optional[str], user_id: Optional[str], value: Optional[str], type: Optional[str], email: Optional[str], subscribed_url: Optional[str], subscribed_referrer: Optional[str], unsubscribed_url: None, unsubscribed_at: None, parent_id: None, ghost_auth_access_token: None, ghost_auth_id: None, password: Optional[str], profile_image: Optional[str], cover_image: Optional[str], bio: Optional[str], website: None, location: Optional[str], facebook: None, twitter: None, accessibility: Optional[str], tour: Optional[str], last_seen: Optional[datetime]) -> None:
        self.key = key
        self.first_request = first_request
        self.last_request = last_request
        self.lifetime = lifetime
        self.count = count
        self.id = id
        self.name = name
        self.version = version
        self.current_version = current_version
        self.lock_key = lock_key
        self.locked = locked
        self.acquired_at = acquired_at
        self.released_at = released_at
        self.post_id = post_id
        self.mobiledoc = mobiledoc
        self.created_at_ts = created_at_ts
        self.created_at = created_at
        self.object_type = object_type
        self.action_type = action_type
        self.object_id = object_id
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.role_id = role_id
        self.permission_id = permission_id
        self.uuid = uuid
        self.title = title
        self.slug = slug
        self.html = html
        self.comment_id = comment_id
        self.plaintext = plaintext
        self.feature_image = feature_image
        self.featured = featured
        self.page = page
        self.status = status
        self.locale = locale
        self.visibility = visibility
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.author_id = author_id
        self.published_at = published_at
        self.published_by = published_by
        self.custom_excerpt = custom_excerpt
        self.codeinjection_head = codeinjection_head
        self.codeinjection_foot = codeinjection_foot
        self.og_image = og_image
        self.og_title = og_title
        self.og_description = og_description
        self.twitter_image = twitter_image
        self.twitter_title = twitter_title
        self.twitter_description = twitter_description
        self.custom_template = custom_template
        self.sort_order = sort_order
        self.tag_id = tag_id
        self.description = description
        self.user_id = user_id
        self.value = value
        self.type = type
        self.email = email
        self.subscribed_url = subscribed_url
        self.subscribed_referrer = subscribed_referrer
        self.unsubscribed_url = unsubscribed_url
        self.unsubscribed_at = unsubscribed_at
        self.parent_id = parent_id
        self.ghost_auth_access_token = ghost_auth_access_token
        self.ghost_auth_id = ghost_auth_id
        self.password = password
        self.profile_image = profile_image
        self.cover_image = cover_image
        self.bio = bio
        self.website = website
        self.location = location
        self.facebook = facebook
        self.twitter = twitter
        self.accessibility = accessibility
        self.tour = tour
        self.last_seen = last_seen


class Meta:
    exported_on: int
    version: str

    def __init__(self, exported_on: int, version: str) -> None:
        self.exported_on = exported_on
        self.version = version


class DB:
    meta: Meta
    data: Dict[str, List[Datum]]

    def __init__(self, meta: Meta, data: Dict[str, List[Datum]]) -> None:
        self.meta = meta
        self.data = data


class Welcome:
    db: List[DB]

    def __init__(self, db: List[DB]) -> None:
        self.db = db
