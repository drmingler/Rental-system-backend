from django.contrib import admin

# Register your models here.
from rentalsystem.chat.models import Chat

common_fields = ["created_at", "updated_at"]


class ChatAdmin(admin.ModelAdmin):
    list_display = [
        "sender",
        "receiver",
        "message",
    ] + common_fields


admin.site.register(Chat, ChatAdmin)
