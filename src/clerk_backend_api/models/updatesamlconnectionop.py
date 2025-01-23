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
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateSAMLConnectionAttributeMappingTypedDict(TypedDict):
    r"""Define the atrtibute name mapping between Identity Provider and Clerk's user properties"""

    user_id: NotRequired[str]
    email_address: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]


class UpdateSAMLConnectionAttributeMapping(BaseModel):
    r"""Define the atrtibute name mapping between Identity Provider and Clerk's user properties"""

    user_id: Optional[str] = None

    email_address: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None


class UpdateSAMLConnectionRequestBodyTypedDict(TypedDict):
    name: NotRequired[Nullable[str]]
    r"""The name of the new SAML Connection"""
    domain: NotRequired[Nullable[str]]
    r"""The domain to use for the new SAML Connection"""
    idp_entity_id: NotRequired[Nullable[str]]
    r"""The entity id as provided by the IdP"""
    idp_sso_url: NotRequired[Nullable[str]]
    r"""The SSO url as provided by the IdP"""
    idp_certificate: NotRequired[Nullable[str]]
    r"""The x509 certificated as provided by the IdP"""
    idp_metadata_url: NotRequired[Nullable[str]]
    r"""The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties and replaces them"""
    idp_metadata: NotRequired[Nullable[str]]
    r"""The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties"""
    organization_id: NotRequired[Nullable[str]]
    r"""The ID of the organization to which users of this SAML Connection will be added"""
    attribute_mapping: NotRequired[
        Nullable[UpdateSAMLConnectionAttributeMappingTypedDict]
    ]
    r"""Define the atrtibute name mapping between Identity Provider and Clerk's user properties"""
    active: NotRequired[Nullable[bool]]
    r"""Activate or de-activate the SAML Connection"""
    sync_user_attributes: NotRequired[Nullable[bool]]
    r"""Controls whether to update the user's attributes in each sign-in"""
    allow_subdomains: NotRequired[Nullable[bool]]
    r"""Allow users with an email address subdomain to use this connection in order to authenticate"""
    allow_idp_initiated: NotRequired[Nullable[bool]]
    r"""Enable or deactivate IdP-initiated flows"""
    disable_additional_identifications: NotRequired[Nullable[bool]]
    r"""Enable or deactivate additional identifications"""


class UpdateSAMLConnectionRequestBody(BaseModel):
    name: OptionalNullable[str] = UNSET
    r"""The name of the new SAML Connection"""

    domain: OptionalNullable[str] = UNSET
    r"""The domain to use for the new SAML Connection"""

    idp_entity_id: OptionalNullable[str] = UNSET
    r"""The entity id as provided by the IdP"""

    idp_sso_url: OptionalNullable[str] = UNSET
    r"""The SSO url as provided by the IdP"""

    idp_certificate: OptionalNullable[str] = UNSET
    r"""The x509 certificated as provided by the IdP"""

    idp_metadata_url: OptionalNullable[str] = UNSET
    r"""The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties and replaces them"""

    idp_metadata: OptionalNullable[str] = UNSET
    r"""The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties"""

    organization_id: OptionalNullable[str] = UNSET
    r"""The ID of the organization to which users of this SAML Connection will be added"""

    attribute_mapping: OptionalNullable[UpdateSAMLConnectionAttributeMapping] = UNSET
    r"""Define the atrtibute name mapping between Identity Provider and Clerk's user properties"""

    active: OptionalNullable[bool] = UNSET
    r"""Activate or de-activate the SAML Connection"""

    sync_user_attributes: OptionalNullable[bool] = UNSET
    r"""Controls whether to update the user's attributes in each sign-in"""

    allow_subdomains: OptionalNullable[bool] = UNSET
    r"""Allow users with an email address subdomain to use this connection in order to authenticate"""

    allow_idp_initiated: OptionalNullable[bool] = UNSET
    r"""Enable or deactivate IdP-initiated flows"""

    disable_additional_identifications: OptionalNullable[bool] = UNSET
    r"""Enable or deactivate additional identifications"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "domain",
            "idp_entity_id",
            "idp_sso_url",
            "idp_certificate",
            "idp_metadata_url",
            "idp_metadata",
            "organization_id",
            "attribute_mapping",
            "active",
            "sync_user_attributes",
            "allow_subdomains",
            "allow_idp_initiated",
            "disable_additional_identifications",
        ]
        nullable_fields = [
            "name",
            "domain",
            "idp_entity_id",
            "idp_sso_url",
            "idp_certificate",
            "idp_metadata_url",
            "idp_metadata",
            "organization_id",
            "attribute_mapping",
            "active",
            "sync_user_attributes",
            "allow_subdomains",
            "allow_idp_initiated",
            "disable_additional_identifications",
        ]
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


class UpdateSAMLConnectionRequestTypedDict(TypedDict):
    saml_connection_id: str
    r"""The ID of the SAML Connection to update"""
    request_body: UpdateSAMLConnectionRequestBodyTypedDict


class UpdateSAMLConnectionRequest(BaseModel):
    saml_connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the SAML Connection to update"""

    request_body: Annotated[
        UpdateSAMLConnectionRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
