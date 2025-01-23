"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from enum import Enum
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateSessionTokenRequestBodyTypedDict(TypedDict):
    expires_in_seconds: NotRequired[Nullable[float]]
    r"""Use this parameter to override the default session token lifetime."""


class CreateSessionTokenRequestBody(BaseModel):
    expires_in_seconds: OptionalNullable[float] = UNSET
    r"""Use this parameter to override the default session token lifetime."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expires_in_seconds"]
        nullable_fields = ["expires_in_seconds"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class CreateSessionTokenRequestTypedDict(TypedDict):
    session_id: str
    r"""The ID of the session"""
    request_body: NotRequired[CreateSessionTokenRequestBodyTypedDict]


class CreateSessionTokenRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the session"""

    request_body: Annotated[
        Optional[CreateSessionTokenRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class CreateSessionTokenObject(str, Enum):
    TOKEN = "token"


class CreateSessionTokenResponseBodyTypedDict(TypedDict):
    r"""OK"""

    object: NotRequired[CreateSessionTokenObject]
    jwt: NotRequired[str]


class CreateSessionTokenResponseBody(BaseModel):
    r"""OK"""

    object: Optional[CreateSessionTokenObject] = None

    jwt: Optional[str] = None
