
from django.contrib.auth.models import User
from rest_framework import serializers
"""Serializers for accounts app."""
from dj_rest_auth.serializers import LoginSerializer, PasswordResetSerializer
from django.conf import settings
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']
        extra_kwargs = {'password': {'write_only': True}}



RESET_PASSWORD_REDIRECT_URL = settings.FRONT_END_URLS.get("PASSWORD_RESET")


def custom_url_generator(request, user, temp_key):
    """Custom url generator for password reset."""
    return f"{RESET_PASSWORD_REDIRECT_URL}/{user.id}/{temp_key}"


class MyLoginSerializer(LoginSerializer):
    """Custom login serializer."""

    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class MyPasswordResetSerializer(PasswordResetSerializer):
    """Custom password reset serializer."""

    def get_email_options(self):
        """Custom email options."""
        return {
            "url_generator": custom_url_generator,
        }
