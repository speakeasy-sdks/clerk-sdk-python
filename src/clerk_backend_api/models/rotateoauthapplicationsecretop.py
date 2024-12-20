"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class RotateOAuthApplicationSecretRequestTypedDict(TypedDict):
    oauth_application_id: str
    r"""The ID of the OAuth application for which to rotate the client secret"""


class RotateOAuthApplicationSecretRequest(BaseModel):
    oauth_application_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the OAuth application for which to rotate the client secret"""
