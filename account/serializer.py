from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.validators import UniqueValidator
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.password_validation import validate_password
import logging
import datetime

logger = logging.getLogger(__name__)

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ("email", "password", "username")

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            username = validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        logger.info(
            f"user {user.username} created." + str(datetime.datetime.now()),
            )
        return user

