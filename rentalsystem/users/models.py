from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, EmailField


class User(AbstractUser):
    """Default user for RentalSystemBackend."""

    #: First and last name do not cover name patterns around the globe
    email = EmailField(max_length=128, blank=True, default=False)

    username = CharField("Username", max_length=255, unique=True)
    birth_date = DateTimeField(max_length=128, blank=True, default=None)
    phone_number = CharField(max_length=20, blank=True, default=None)
    address = CharField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "country"]
