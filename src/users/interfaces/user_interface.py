from abc import ABC, abstractmethod
from django.contrib.auth.base_user import AbstractBaseUser


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create(self, email: str, password: str) -> AbstractBaseUser:
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def email_exists(self, email: str) -> bool:
        pass


