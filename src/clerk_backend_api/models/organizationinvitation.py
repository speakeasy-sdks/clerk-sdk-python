"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict


class OrganizationInvitationObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    ORGANIZATION_INVITATION = "organization_invitation"


class OrganizationInvitationTypedDict(TypedDict):
    r"""An organization invitation"""

    id: NotRequired[str]
    object: NotRequired[OrganizationInvitationObject]
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    email_address: NotRequired[str]
    role: NotRequired[str]
    role_name: NotRequired[str]
    organization_id: NotRequired[str]
    status: NotRequired[str]
    public_metadata: NotRequired[Dict[str, Any]]
    private_metadata: NotRequired[Dict[str, Any]]
    url: NotRequired[Nullable[str]]
    expires_at: NotRequired[Nullable[int]]
    r"""Unix timestamp of expiration.

    """
    created_at: NotRequired[int]
    r"""Unix timestamp of creation."""
    updated_at: NotRequired[int]
    r"""Unix timestamp of last update."""


class OrganizationInvitation(BaseModel):
    r"""An organization invitation"""

    id: Optional[str] = None

    object: Optional[OrganizationInvitationObject] = None
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    email_address: Optional[str] = None

    role: Optional[str] = None

    role_name: Optional[str] = None

    organization_id: Optional[str] = None

    status: Optional[str] = None

    public_metadata: Optional[Dict[str, Any]] = None

    private_metadata: Optional[Dict[str, Any]] = None

    url: OptionalNullable[str] = UNSET

    expires_at: OptionalNullable[int] = UNSET
    r"""Unix timestamp of expiration.

    """

    created_at: Optional[int] = None
    r"""Unix timestamp of creation."""

    updated_at: Optional[int] = None
    r"""Unix timestamp of last update."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "object",
            "email_address",
            "role",
            "role_name",
            "organization_id",
            "status",
            "public_metadata",
            "private_metadata",
            "url",
            "expires_at",
            "created_at",
            "updated_at",
        ]
        nullable_fields = ["url", "expires_at"]
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
