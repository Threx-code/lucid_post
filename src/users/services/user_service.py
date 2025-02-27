from django.contrib.auth import authenticate
from knox.models import AuthToken
from ..interfaces.user_interface import UserRepositoryInterface

class UserService:

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository


    def create(self, email: str, password: str):
        user = self.repository.create(email, password)
        return user, AuthToken.objects.create(user)[1]


    def get_all(self):
        return self.repository.get_all()


    def email_exists(self, email: str) -> bool:
        return self.repository.email_exists(email)


    def login(self, email: str, password: str):
        user = authenticate(email=email, password=password)
        if not user:
            return None, None
        return user, AuthToken.objects.create(user)[1]
