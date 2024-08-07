"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateOrganizationInvitationPublicMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API."""
    
    

class CreateOrganizationInvitationPublicMetadata(BaseModel):
    r"""Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API."""
    
    

class CreateOrganizationInvitationPrivateMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API."""
    
    

class CreateOrganizationInvitationPrivateMetadata(BaseModel):
    r"""Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API."""
    
    

class CreateOrganizationInvitationRequestBodyTypedDict(TypedDict):
    email_address: str
    r"""The email address of the new member that is going to be invited to the organization"""
    inviter_user_id: str
    r"""The ID of the user that invites the new member to the organization.
    Must be an administrator in the organization.
    """
    role: str
    r"""The role of the new member in the organization"""
    public_metadata: NotRequired[CreateOrganizationInvitationPublicMetadataTypedDict]
    r"""Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API."""
    private_metadata: NotRequired[CreateOrganizationInvitationPrivateMetadataTypedDict]
    r"""Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API."""
    redirect_url: NotRequired[str]
    r"""Optional URL that the invitee will be redirected to once they accept the invitation by clicking the join link in the invitation email."""
    

class CreateOrganizationInvitationRequestBody(BaseModel):
    email_address: str
    r"""The email address of the new member that is going to be invited to the organization"""
    inviter_user_id: str
    r"""The ID of the user that invites the new member to the organization.
    Must be an administrator in the organization.
    """
    role: str
    r"""The role of the new member in the organization"""
    public_metadata: Optional[CreateOrganizationInvitationPublicMetadata] = None
    r"""Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API."""
    private_metadata: Optional[CreateOrganizationInvitationPrivateMetadata] = None
    r"""Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API."""
    redirect_url: Optional[str] = None
    r"""Optional URL that the invitee will be redirected to once they accept the invitation by clicking the join link in the invitation email."""
    

class CreateOrganizationInvitationRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID of the organization for which to send the invitation"""
    request_body: CreateOrganizationInvitationRequestBodyTypedDict
    

class CreateOrganizationInvitationRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the organization for which to send the invitation"""
    request_body: Annotated[CreateOrganizationInvitationRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
