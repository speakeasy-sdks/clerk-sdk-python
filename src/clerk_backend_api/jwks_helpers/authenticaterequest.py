import httpx
from dataclasses import dataclass
from enum import Enum
from http.cookies import SimpleCookie
from typing import List, Union, Optional
from warnings import warn

from ..sdk import Clerk
from .verifytoken import TokenVerificationErrorReason, TokenVerificationError, VerifyTokenOptions, verify_token


class AuthErrorReason(Enum):

    SESSION_TOKEN_MISSING = (
        'session-token-missing',
        'Could not retrieve session token. Please make sure that the __session cookie or the HTTP authorization header contain a Clerk-generated session JWT',
    )

    SECRET_KEY_MISSING = (
        'secret-key-missing',
        'Missing Clerk Secret Key. Go to https://dashboard.clerk.com and get your key for your instance.'
    )


class AuthStatus(Enum):
    """Authentication Status"""

    SIGNED_IN = 'signed-in'
    SIGNED_OUT = 'signed-out'


@dataclass
class RequestState:
    """Request Authentication State"""

    status: AuthStatus
    reason: Optional[Union[AuthErrorReason, TokenVerificationErrorReason]] = None
    token: Optional[str] = None

    @property
    def is_signed_in(self) -> bool:
        return self.status == AuthStatus.SIGNED_IN

    @property
    def message(self) -> Optional[str]:
        if self.reason is None:
            return None
        return self.reason.value[1]


@dataclass
class AuthenticateRequestOptions:
    """
    Options to configure authenticate_request.

    Attributes:
        secret_key (Optional[str]): The Clerk secret key from the API Keys page in the Clerk Dashboard.
        jwt_key (Optional[str]): Used to verify the session token in a networkless manner.
        audience (Union[str, List[str], None]): An audience or list of audiences to verify against.
        authorized_parties (Optional[List[str]]): An allowlist of origins to verify against.
        clock_skew_in_ms (int): Allowed time difference (in milliseconds) between the Clerk server (which generates the token)
                                and the clock of the user's application server when validating a token. Defaults to 5000 ms.
    """

    secret_key: Optional[str] = None
    jwt_key: Optional[str] = None
    audience: Union[str, List[str], None] = None
    authorized_parties: Optional[List[str]] = None
    clock_skew_in_ms: int = 5000

def authenticate_request(self: Clerk, request: httpx.Request, options: AuthenticateRequestOptions) -> RequestState:
    """ Authenticates the session token. Networkless if the options.jwt_key is provided.
    Otherwise, performs a network call to retrieve the JWKS from Clerk's Backend API.
    """

    warn('authenticate_request method is applicable in the context of Backend APIs only.')

    def get_secret_key(clerk: Clerk, options) -> Optional[str]:
        """If not provided, try retrieving the secret_key from the SDK security """

        if options.secret_key is not None:
            return options.secret_key

        security = clerk.sdk_configuration.security
        if security is None:
            return None

        # WARNING: this relies on bearerAuth being the only security scheme
        if callable(security):
            return security().bearer_auth
        return security.bearer_auth


    def get_session_token(request) -> Optional[str]:
        """Retrieve token from __session cookie or Authorization header."""

        # https://github.com/clerk/javascript/blob/main/packages/backend/src/tokens/request.ts#L343
        bearer_token = request.headers.get('Authorization')
        if bearer_token is not None:
            return bearer_token.replace('Bearer ', '')

        # https://github.com/clerk/javascript/blob/main/packages/backend/src/tokens/request.ts#L386
        cookie_header = request.headers.get('cookie')
        if cookie_header is not None:
            session_cookie = SimpleCookie(cookie_header).get('__session')
            if session_cookie is not None:
                return session_cookie.value

        return None


    session_token = get_session_token(request)
    if session_token is None:
        return RequestState(status=AuthStatus.SIGNED_OUT, reason=AuthErrorReason.SESSION_TOKEN_MISSING)

    secret_key = get_secret_key(self, options)
    if secret_key is None:
        return RequestState(status=AuthStatus.SIGNED_OUT, reason=AuthErrorReason.SECRET_KEY_MISSING)

    try:
        verify_token(
            session_token,
            VerifyTokenOptions(
                audience=options.audience,
                authorized_parties=options.authorized_parties,
                secret_key=secret_key,
                clock_skew_in_ms=options.clock_skew_in_ms,
                jwt_key=options.jwt_key,
            ),
        )

        return RequestState(status=AuthStatus.SIGNED_IN, token=session_token)

    except TokenVerificationError as e:
        return RequestState(status=AuthStatus.SIGNED_OUT, reason=e.reason)