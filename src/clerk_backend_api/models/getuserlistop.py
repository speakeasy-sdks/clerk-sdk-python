"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetUserListRequestTypedDict(TypedDict):
    email_address: NotRequired[List[str]]
    r"""Returns users with the specified email addresses.
    Accepts up to 100 email addresses.
    Any email addresses not found are ignored.
    """
    phone_number: NotRequired[List[str]]
    r"""Returns users with the specified phone numbers.
    Accepts up to 100 phone numbers.
    Any phone numbers not found are ignored.
    """
    external_id: NotRequired[List[str]]
    r"""Returns users with the specified external ids.
    For each external id, the `+` and `-` can be
    prepended to the id, which denote whether the
    respective external id should be included or
    excluded from the result set.
    Accepts up to 100 external ids.
    Any external ids not found are ignored.
    """
    username: NotRequired[List[str]]
    r"""Returns users with the specified usernames.
    Accepts up to 100 usernames.
    Any usernames not found are ignored.
    """
    web3_wallet: NotRequired[List[str]]
    r"""Returns users with the specified web3 wallet addresses.
    Accepts up to 100 web3 wallet addresses.
    Any web3 wallet addressed not found are ignored.
    """
    user_id: NotRequired[List[str]]
    r"""Returns users with the user ids specified.
    For each user id, the `+` and `-` can be
    prepended to the id, which denote whether the
    respective user id should be included or
    excluded from the result set.
    Accepts up to 100 user ids.
    Any user ids not found are ignored.
    """
    organization_id: NotRequired[List[str]]
    r"""Returns users that have memberships to the
    given organizations.
    For each organization id, the `+` and `-` can be
    prepended to the id, which denote whether the
    respective organization should be included or
    excluded from the result set.
    Accepts up to 100 organization ids.
    """
    query: NotRequired[str]
    r"""Returns users that match the given query.
    For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names.
    The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well.
    """
    email_address_query: NotRequired[str]
    r"""Returns users with emails that match the given query, via case-insensitive partial match.
    For example, `email_address_query=ello` will match a user with the email `HELLO@example.com`.
    """
    phone_number_query: NotRequired[str]
    r"""Returns users with phone numbers that match the given query, via case-insensitive partial match.
    For example, `phone_number_query=555` will match a user with the phone number `+1555xxxxxxx`.
    """
    username_query: NotRequired[str]
    r"""Returns users with usernames that match the given query, via case-insensitive partial match.
    For example, `username_query=CoolUser` will match a user with the username `SomeCoolUser`.
    """
    name_query: NotRequired[str]
    r"""Returns users with names that match the given query, via case-insensitive partial match."""
    last_active_at_before: NotRequired[int]
    r"""Returns users whose last session activity was before the given date (with millisecond precision).
    Example: use 1700690400000 to retrieve users whose last session activity was before 2023-11-23.
    """
    last_active_at_after: NotRequired[int]
    r"""Returns users whose last session activity was after the given date (with millisecond precision).
    Example: use 1700690400000 to retrieve users whose last session activity was after 2023-11-23.
    """
    last_active_at_since: NotRequired[int]
    r"""Returns users that had session activity since the given date.
    Example: use 1700690400000 to retrieve users that had session activity from 2023-11-23 until the current day.
    Deprecated in favor of `last_active_at_after`.
    """
    created_at_before: NotRequired[int]
    r"""Returns users who have been created before the given date (with millisecond precision).
    Example: use 1730160000000 to retrieve users who have been created before 2024-10-29.
    """
    created_at_after: NotRequired[int]
    r"""Returns users who have been created after the given date (with millisecond precision).
    Example: use 1730160000000 to retrieve users who have been created after 2024-10-29.
    """
    limit: NotRequired[int]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[int]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    order_by: NotRequired[str]
    r"""Allows to return users in a particular order.
    At the moment, you can order the returned users by their `created_at`,`updated_at`,`email_address`,`web3wallet`,`first_name`,`last_name`,`phone_number`,`username`,`last_active_at`,`last_sign_in_at`.
    In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.
    For example, if you want users to be returned in descending order according to their `created_at` property, you can use `-created_at`.
    If you don't use `+` or `-`, then `+` is implied. We only support one `order_by` parameter, and if multiple `order_by` parameters are provided, we will only keep the first one. For example,
    if you pass `order_by=username&order_by=created_at`, we will consider only the first `order_by` parameter, which is `username`. The `created_at` parameter will be ignored in this case.
    """


class GetUserListRequest(BaseModel):
    email_address: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with the specified email addresses.
    Accepts up to 100 email addresses.
    Any email addresses not found are ignored.
    """

    phone_number: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with the specified phone numbers.
    Accepts up to 100 phone numbers.
    Any phone numbers not found are ignored.
    """

    external_id: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with the specified external ids.
    For each external id, the `+` and `-` can be
    prepended to the id, which denote whether the
    respective external id should be included or
    excluded from the result set.
    Accepts up to 100 external ids.
    Any external ids not found are ignored.
    """

    username: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with the specified usernames.
    Accepts up to 100 usernames.
    Any usernames not found are ignored.
    """

    web3_wallet: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with the specified web3 wallet addresses.
    Accepts up to 100 web3 wallet addresses.
    Any web3 wallet addressed not found are ignored.
    """

    user_id: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with the user ids specified.
    For each user id, the `+` and `-` can be
    prepended to the id, which denote whether the
    respective user id should be included or
    excluded from the result set.
    Accepts up to 100 user ids.
    Any user ids not found are ignored.
    """

    organization_id: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users that have memberships to the
    given organizations.
    For each organization id, the `+` and `-` can be
    prepended to the id, which denote whether the
    respective organization should be included or
    excluded from the result set.
    Accepts up to 100 organization ids.
    """

    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users that match the given query.
    For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names.
    The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well.
    """

    email_address_query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with emails that match the given query, via case-insensitive partial match.
    For example, `email_address_query=ello` will match a user with the email `HELLO@example.com`.
    """

    phone_number_query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with phone numbers that match the given query, via case-insensitive partial match.
    For example, `phone_number_query=555` will match a user with the phone number `+1555xxxxxxx`.
    """

    username_query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with usernames that match the given query, via case-insensitive partial match.
    For example, `username_query=CoolUser` will match a user with the username `SomeCoolUser`.
    """

    name_query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users with names that match the given query, via case-insensitive partial match."""

    last_active_at_before: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users whose last session activity was before the given date (with millisecond precision).
    Example: use 1700690400000 to retrieve users whose last session activity was before 2023-11-23.
    """

    last_active_at_after: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users whose last session activity was after the given date (with millisecond precision).
    Example: use 1700690400000 to retrieve users whose last session activity was after 2023-11-23.
    """

    last_active_at_since: Annotated[
        Optional[int],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users that had session activity since the given date.
    Example: use 1700690400000 to retrieve users that had session activity from 2023-11-23 until the current day.
    Deprecated in favor of `last_active_at_after`.
    """

    created_at_before: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users who have been created before the given date (with millisecond precision).
    Example: use 1730160000000 to retrieve users who have been created before 2024-10-29.
    """

    created_at_after: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Returns users who have been created after the given date (with millisecond precision).
    Example: use 1730160000000 to retrieve users who have been created after 2024-10-29.
    """

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """

    order_by: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "-created_at"
    r"""Allows to return users in a particular order.
    At the moment, you can order the returned users by their `created_at`,`updated_at`,`email_address`,`web3wallet`,`first_name`,`last_name`,`phone_number`,`username`,`last_active_at`,`last_sign_in_at`.
    In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.
    For example, if you want users to be returned in descending order according to their `created_at` property, you can use `-created_at`.
    If you don't use `+` or `-`, then `+` is implied. We only support one `order_by` parameter, and if multiple `order_by` parameters are provided, we will only keep the first one. For example,
    if you pass `order_by=username&order_by=created_at`, we will consider only the first `order_by` parameter, which is `username`. The `created_at` parameter will be ignored in this case.
    """
