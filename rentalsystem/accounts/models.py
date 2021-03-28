from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, EmailField, ImageField

from rentalsystem.common.models import AbstractBaseModel
from rentalsystem.utils.storages import MediaRootS3Boto3Storage


class User(AbstractUser, AbstractBaseModel):
    """Default user for RentalSystemBackend."""

    FEMALE = "Female"
    MALE = "Male"
    GENDER_CHOICE = [(MALE, "Male"), (FEMALE, "Female")]

    LANDLORD = "Landlord"
    TENANT = "Tenant"
    USER_TYPE = [(LANDLORD, "Landlord"), (TENANT, "Tenant")]

    email = EmailField(max_length=150, unique=True)
    username = CharField(max_length=255, unique=True)
    phoneNumber = CharField("Phone number", max_length=20, blank=True)
    birthDate = DateTimeField("Birth date", max_length=128, blank=True)
    userType = CharField("User type", choices=USER_TYPE, max_length=30, default=TENANT)
    avatar = ImageField(blank=True, storage=MediaRootS3Boto3Storage())
    gender = CharField(choices=GENDER_CHOICE, max_length=30, blank=True)
    address = CharField(blank=True, max_length=255)
    nationality = CharField(blank=True, max_length=40)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]
