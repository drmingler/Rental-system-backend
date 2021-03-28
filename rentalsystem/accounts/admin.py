from django.contrib import admin

from rentalsystem.accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "username",
        "phoneNumber",
        "birthDate",
        "avatar",
        "gender",
        "userType",
        "address",
        "nationality",
    ]


admin.site.register(User, UserAdmin)
