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


class OrganizationObject(str, Enum):
    ORGANIZATION = "organization"


class OrganizationTypedDict(TypedDict):
    object: OrganizationObject
    id: str
    name: str
    slug: str
    max_allowed_memberships: int
    public_metadata: Dict[str, Any]
    private_metadata: Dict[str, Any]
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    members_count: NotRequired[Nullable[int]]
    admin_delete_enabled: NotRequired[bool]
    created_by: NotRequired[Nullable[str]]


class Organization(BaseModel):
    object: OrganizationObject

    id: str

    name: str

    slug: str

    max_allowed_memberships: int

    public_metadata: Dict[str, Any]

    private_metadata: Dict[str, Any]

    created_at: int
    r"""Unix timestamp of creation.

    """

    updated_at: int
    r"""Unix timestamp of last update.

    """

    members_count: OptionalNullable[int] = UNSET

    admin_delete_enabled: Optional[bool] = None

    created_by: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["members_count", "admin_delete_enabled", "created_by"]
        nullable_fields = ["members_count", "created_by"]
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
