from rest_framework import serializers
from django.contrib.auth import authenticate, get_user


class Serializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email').lower()
        password = attrs.get('password')
        if not email or not password:
            raise serializers.ValidationError('Email and password are required')

        user = authenticate(self.context.get('request'), email=email, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        attrs['user'] = user
        return attrs