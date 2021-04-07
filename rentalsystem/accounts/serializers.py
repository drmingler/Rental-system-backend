from rest_framework import serializers

from rentalsystem.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")

    class Meta:
        model = User
        fields = [
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
        read_only_fields = [
            User.ID,
            User.EMAIL,
            User.USERNAME,
        ]
