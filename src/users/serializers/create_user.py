from rest_framework import serializers
from .password_validation import PasswordValidation
from ..models import User
from ..repositories.user_repository import UserRepository
from ..services.user_service import UserService


class CreateUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    full_name = serializers.CharField(required=True, max_length=255)

    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {
            "password":{"write_only": True}
        }


    def validate_email(self, value):
        email = value.strip().lower()
        if UserService(UserRepository()).email_exists(email):
            raise serializers.ValidationError("Email already exist")
        return email


    def validate_password(self, password):
        email = self.initial_data.get("email", "").strip().lower()
        return PasswordValidation(password, email).validate()
