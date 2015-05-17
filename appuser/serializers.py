from rest_framework import serializers
import appuser.models as models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Login
