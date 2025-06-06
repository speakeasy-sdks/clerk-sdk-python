"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from typing_extensions import TypedDict


class CreateRedirectURLRequestBodyTypedDict(TypedDict):
    url: str
    r"""The full url value prefixed with `https://` or a custom scheme e.g. `\"https://my-app.com/oauth-callback\"` or `\"my-app://oauth-callback\"`"""


class CreateRedirectURLRequestBody(BaseModel):
    url: str
    r"""The full url value prefixed with `https://` or a custom scheme e.g. `\"https://my-app.com/oauth-callback\"` or `\"my-app://oauth-callback\"`"""
