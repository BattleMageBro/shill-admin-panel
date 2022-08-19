from django.db import models
from django.contrib.postgres.fields import ArrayField


class Chat(models.Model):
    #chat_uuid = models.BigIntegerField(primary_key=True)
    chat_name = models.CharField(max_length=512, blank=True)
    shill_message = models.TextField(blank=True, null=True)
    shill_links = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    shill_timeout = models.IntegerField(default=60)
    msg_timeout = models.IntegerField(default=1)
    shill_end = models.FloatField(default=1)
    
    class Meta:
        verbose_name_plural = 'Chats'


class Users(models.Model):
    #user_uuid = models.BigIntegerField(primary_key=True)
    current_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ShillUsers'


class UserChat(models.Model):
    chat_uuid = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user_uuid = models.ForeignKey(Users, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'UserChat_sequence'

class Packs(models.Model):
    #pack_uuid = models.AutoField(primary_key=True)
    pack_description = models.TextField(blank=True)
    shill_links = ArrayField(models.CharField(max_length=255), blank=True)
    class Meta:
        verbose_name_plural = 'Packs'