from ..interfaces.user_interface import UserRepositoryInterface
from ..models import User
from django.contrib.auth.models import AbstractBaseUser

class UserRepository(UserRepositoryInterface):

    def __init__(self):
        self.user = User


    def create(self, email: str, password: str) -> AbstractBaseUser:
        return self.user.objects.create_user(
            email=email,
            password=password
        )


    def get_all(self):
        return self.user.objects.all()

    def email_exists(self, email: str) -> bool:
        return self.user.objects.filter(email=email).exists()

