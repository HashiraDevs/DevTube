from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']
        extra_kwargs = {'password': {'write_only': True}}