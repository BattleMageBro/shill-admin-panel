from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from admin_panel.models import Chat, Users, Packs, UserChat



@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_name', 'shill_message')
    search_fields = ("chat_name__startswith", )


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_chat_id')


@admin.register(Packs)
class PacksAdmin(admin.ModelAdmin):
    list_display = ('id', 'pack_description')

@admin.register(UserChat)
class UserChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_uuid_id', 'chat_uuid_id')
    list_filter = ('user_uuid_id', 'chat_uuid_id')

