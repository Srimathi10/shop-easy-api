"""Customer accounts."""
from dataclasses import dataclass
from itertools import count
from typing import Dict, Optional


@dataclass
class User:
    id: int
    email: str
    name: str
    password_hash: str
    is_active: bool = True


class UserRepository:
    """In-memory user store. Production uses a database behind the same interface."""

    def __init__(self) -> None:
        self._users: Dict[str, User] = {}
        self._ids = count(1)

    @staticmethod
    def _key(email: str) -> str:
        return email.strip().lower()

    def add(self, email: str, name: str, password_hash: str) -> User:
        key = self._key(email)
        if key in self._users:
            raise ValueError(f"User already exists: {email}")
        user = User(id=next(self._ids), email=key, name=name, password_hash=password_hash)
        self._users[key] = user
        return user

    def get_by_email(self, email: str) -> Optional[User]:
        return self._users.get(self._key(email))

    def save(self, user: User) -> None:
        self._users[self._key(user.email)] = user

    def __len__(self) -> int:
        return len(self._users)
