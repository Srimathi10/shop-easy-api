import pytest

from src.user import UserRepository


def test_add_and_find_user_is_case_insensitive():
    users = UserRepository()
    users.add("Priya@ShopEasy.example", "Priya", "hash")
    assert users.get_by_email("  priya@shopeasy.example ").name == "Priya"


def test_duplicate_email_is_rejected():
    users = UserRepository()
    users.add("david@shopeasy.example", "David", "hash")
    with pytest.raises(ValueError):
        users.add("DAVID@shopeasy.example", "David again", "hash")


def test_unknown_email_returns_none():
    assert UserRepository().get_by_email("nobody@shopeasy.example") is None
