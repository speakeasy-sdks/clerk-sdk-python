"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VerifyPasswordRequestBodyTypedDict(TypedDict):
    password: str
    r"""The user password to verify"""


class VerifyPasswordRequestBody(BaseModel):
    password: str
    r"""The user password to verify"""


class VerifyPasswordRequestTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user for whom to verify the password"""
    request_body: NotRequired[VerifyPasswordRequestBodyTypedDict]


class VerifyPasswordRequest(BaseModel):
    user_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the user for whom to verify the password"""

    request_body: Annotated[
        Optional[VerifyPasswordRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class VerifyPasswordResponseBodyTypedDict(TypedDict):
    r"""The provided password was correct."""

    verified: NotRequired[bool]


class VerifyPasswordResponseBody(BaseModel):
    r"""The provided password was correct."""

    verified: Optional[bool] = None
