from rest_framework import serializers

from rentalsystem.accounts.models import User
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
]
READ_ONLY_FIELDS = [User.ID, User.EMAIL, User.USERNAME]


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")

    class Meta:
        model = User
        fields = COMMON_PROPERTY_FIELDS
        read_only_fields = READ_ONLY_FIELDS


class LandlordSerializer(serializers.ModelSerializer):
    numberOfProperties = serializers.SerializerMethodField()
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")

    class Meta:
        model = User
        fields = COMMON_PROPERTY_FIELDS + ["numberOfProperties"]
        read_only_fields = READ_ONLY_FIELDS

    def get_numberOfProperties(self, instance) -> int:
        return Property.objects.filter(landlord=instance.id).count()
