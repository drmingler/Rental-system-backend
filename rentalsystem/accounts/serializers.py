from django.db import transaction
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from rentalsystem.accounts.models import User
from rentalsystem.accounts.utils import generate_username
from rentalsystem.properties.models import Property

COMMON_PROPERTY_FIELDS = [
    User.ID,
    User.EMAIL,
    User.USERNAME,
    User.FIRST_NAME,
    User.LAST_NAME,
    User.PHONE_NUMBER,
    User.BIRTH_DATE,
    User.AVATAR,
    User.GENDER,
    User.USER_TYPE,
    User.ADDRESS,
    User.NATIONALITY,
    User.BIO,
    User.OCCUPATION,
]
READ_ONLY_FIELDS = [User.ID, User.EMAIL, User.USERNAME]


class AbstractUserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    pass


class UserSerializer(AbstractUserSerializer):
    class Meta:
        model = User
        fields = COMMON_PROPERTY_FIELDS
        read_only_fields = READ_ONLY_FIELDS


class SimpleUserSerializer(AbstractUserSerializer):
    class Meta:
        model = User
        fields = [
            User.ID,
            User.EMAIL,
            User.USERNAME,
            User.FIRST_NAME,
            User.ADDRESS,
            User.NATIONALITY,
            User.AVATAR,
        ]


class LandlordSerializer(AbstractUserSerializer):
    numberOfProperties = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            User.ID,
            User.EMAIL,
            User.USERNAME,
            User.FIRST_NAME,
            User.ADDRESS,
            User.NATIONALITY,
            User.AVATAR,
            "numberOfProperties",
        ]
        read_only_fields = READ_ONLY_FIELDS

    def get_numberOfProperties(self, instance) -> int:
        return Property.objects.filter(landlord=instance.id).count()


class CustomUserCreateSerializer(AbstractUserSerializer, UserCreateSerializer):
    class Meta:
        model = User
        fields = [
            User.EMAIL,
            User.FIRST_NAME,
            User.LAST_NAME,
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
        ]

    def perform_create(self, validated_data):
        with transaction.atomic():
            username = generate_username(
                first_name=validated_data["first_name"], email=validated_data["email"]
            )
            validated_data.update({"username": username})
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user
