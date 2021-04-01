from rest_framework.permissions import BasePermission

from rentalsystem.accounts.models import User


class AbstractBasePermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user and request.user.is_authenticated


class IsOwner(AbstractBasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        return request.user == obj.user


class IsOwnProfile(AbstractBasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.id == obj.id


class IsLandlord(AbstractBasePermission):
    """
    Custom permission to only allow landlords to add and edit properties.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        user: User = request.user
        return user.userType == User.LANDLORD and user == obj.landlord
