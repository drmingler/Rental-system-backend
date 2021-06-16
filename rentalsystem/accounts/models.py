from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, EmailField, ImageField
from django.db.models.fields import TextField, DateField

from rentalsystem.common.models import AbstractBaseModel
from rentalsystem.utils.storages import MediaRootS3Boto3Storage


class User(AbstractUser, AbstractBaseModel):
    """Default user for RentalSystemBackend."""

    ID = "id"
    EMAIL = "email"
    USERNAME = "username"
    FIRST_NAME = "firstName"
    LAST_NAME = "lastName"
    PHONE_NUMBER = "phoneNumber"
    BIRTH_DATE = "birthDate"
    USER_TYPE = "userType"
    AVATAR = "avatar"
    GENDER = "gender"
    ADDRESS = "address"
    NATIONALITY = "nationality"
    BIO = "bio"
    OCCUPATION = "occupation"
    FEMALE = "FEMALE"
    MALE = "MALE"
    LANDLORD = "LANDLORD"
    TENANT = "TENANT"

    GENDER_CHOICE = [(MALE, "MALE"), (FEMALE, "FEMALE")]
    USER_TYPES = [(LANDLORD, "LANDLORD"), (TENANT, "TENANT")]

    email = EmailField(max_length=150, unique=True)
    phoneNumber = CharField("Phone number", max_length=20, blank=True)
    birthDate = DateField("Birth date", max_length=128, blank=True, null=True)
    userType = CharField(
        "User type", choices=USER_TYPES, max_length=30, default=TENANT, blank=True
    )
    avatar = ImageField(blank=True, storage=MediaRootS3Boto3Storage())
    gender = CharField(choices=GENDER_CHOICE, max_length=30, blank=True)
    address = CharField(blank=True, max_length=255)
    nationality = CharField(blank=True, max_length=40)
    bio = TextField(blank=True)
    occupation = CharField(blank=True, max_length=40)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def save(self, *args, **kwargs):
        if "" not in [self.gender, self.nationality, self.address]:
            self.userType = self.LANDLORD
        super(User, self).save(*args, **kwargs)
