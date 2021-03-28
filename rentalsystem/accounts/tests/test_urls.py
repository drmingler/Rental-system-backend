import pytest
from django.urls import resolve, reverse

from rentalsystem.accounts.models import User

pytestmark = pytest.mark.django_db


def test_detail(user: User):
    assert (
        reverse("accounts:detail", kwargs={"username": user.username})
        == f"/accounts/{user.username}/"
    )
    assert resolve(f"/accounts/{user.username}/").view_name == "accounts:detail"


def test_update():
    assert reverse("accounts:update") == "/accounts/~update/"
    assert resolve("/accounts/~update/").view_name == "accounts:update"


def test_redirect():
    assert reverse("accounts:redirect") == "/accounts/~redirect/"
    assert resolve("/accounts/~redirect/").view_name == "accounts:redirect"
