import pytest
from django.urls import resolve, reverse

from rentalsystem.accounts.models import User

pytestmark = pytest.mark.django_db


def test_user_detail(user: User):
    assert (
        reverse("api:user-detail", kwargs={"username": user.username})
        == f"/api/accounts/{user.username}/"
    )
    assert resolve(f"/api/accounts/{user.username}/").view_name == "api:user-detail"


def test_user_list():
    assert reverse("api:user-list") == "/api/accounts/"
    assert resolve("/api/accounts/").view_name == "api:user-list"


def test_user_me():
    assert reverse("api:user-me") == "/api/accounts/me/"
    assert resolve("/api/accounts/me/").view_name == "api:user-me"
