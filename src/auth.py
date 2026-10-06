"""Authentication: password hashing and login."""
import hashlib
import hmac
import os

from .logger import get_logger
from .user import User, UserRepository

log = get_logger("auth")

_ITERATIONS = 100_000
MIN_PASSWORD_LENGTH = 8


class AuthenticationError(Exception):
    """Raised when an email/password combination is not accepted."""


def hash_password(password: str) -> str:
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValueError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters")
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, _ITERATIONS)
    return f"{salt.hex()}${digest.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    salt_hex, digest_hex = stored_hash.split("$")
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt_hex), _ITERATIONS)
    return hmac.compare_digest(digest.hex(), digest_hex)


def login(users: UserRepository, email: str, password: str) -> User:
    user = users.get_by_email(email)
    if user is None or not user.is_active or not verify_password(password, user.password_hash):
        log.warning("Failed login attempt")
        raise AuthenticationError("Invalid email or password")
    log.info("User %s logged in", user.id)
    return user
