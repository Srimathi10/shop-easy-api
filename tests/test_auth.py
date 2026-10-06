import pytest

from src.auth import AuthenticationError, hash_password, login, verify_password
from src.user import UserRepository


@pytest.fixture
def users():
    repo = UserRepository()
    repo.add("priya@shopeasy.example", "Priya", hash_password("correct-horse-42"))
    return repo


def test_password_hash_round_trip():
    stored = hash_password("correct-horse-42")
    assert verify_password("correct-horse-42", stored)
    assert not verify_password("wrong-password", stored)


def test_short_passwords_are_rejected():
    with pytest.raises(ValueError):
        hash_password("short")


def test_login_with_correct_password(users):
    assert login(users, "priya@shopeasy.example", "correct-horse-42").name == "Priya"


def test_login_with_wrong_password_fails(users):
    with pytest.raises(AuthenticationError):
        login(users, "priya@shopeasy.example", "wrong-password")


def test_login_for_unknown_user_fails(users):
    with pytest.raises(AuthenticationError):
        login(users, "nobody@shopeasy.example", "correct-horse-42")
