"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateOAuthApplicationRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The new name of the OAuth application"""
    callback_url: NotRequired[str]
    r"""The new callback URL of the OAuth application"""
    scopes: NotRequired[str]
    r"""Define the allowed scopes for the new OAuth applications that dictate the user payload of the OAuth user info endpoint. Available scopes are `profile`, `email`, `public_metadata`, `private_metadata`. Provide the requested scopes as a string, separated by spaces."""
    

class UpdateOAuthApplicationRequestBody(BaseModel):
    name: Optional[str] = None
    r"""The new name of the OAuth application"""
    callback_url: Optional[str] = None
    r"""The new callback URL of the OAuth application"""
    scopes: Optional[str] = "profile email"
    r"""Define the allowed scopes for the new OAuth applications that dictate the user payload of the OAuth user info endpoint. Available scopes are `profile`, `email`, `public_metadata`, `private_metadata`. Provide the requested scopes as a string, separated by spaces."""
    

class UpdateOAuthApplicationRequestTypedDict(TypedDict):
    oauth_application_id: str
    r"""The ID of the OAuth application to update"""
    request_body: UpdateOAuthApplicationRequestBodyTypedDict
    

class UpdateOAuthApplicationRequest(BaseModel):
    oauth_application_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the OAuth application to update"""
    request_body: Annotated[UpdateOAuthApplicationRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
