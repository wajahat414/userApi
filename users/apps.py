from django.apps import AppConfig

from rest_framework import serializers


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
