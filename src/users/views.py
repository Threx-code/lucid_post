from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import login
from .repositories.user_repository import UserRepository
from .serializers.create_user_success import UserSerializer
from .services.user_service import UserService
from .serializers import (
create_user as create_serializer, login as login_serializer
)


class UserRegistrationAPI(CreateAPIView):
    queryset = UserService(UserRepository()).get_all()
    serializer_class = create_serializer.CreateUserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_service = UserService(UserRepository())

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user, token = user_service.create(email, password)

        return Response(
            {
                'message': 'User has been successfully registered',
                'user': UserSerializer(user).data,
                'token': token
            },
            status=status.HTTP_201_CREATED
        )



class UserLoginViewAPI(KnoxLoginView):
    permission_classes = (AllowAny,)
    serializer_class = login_serializer.Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, *args, **kwargs)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response(response.data, status=status.HTTP_200_OK)