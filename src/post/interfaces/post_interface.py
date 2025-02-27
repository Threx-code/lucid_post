from abc import ABC, abstractmethod
from django.contrib.auth.base_user import AbstractBaseUser


class PostRepositoryInterface(ABC):

    @abstractmethod
    def create(self, user, text):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_posts(self, user) -> bool:
        pass

    def delete_post(self, user, post_id):
        pass


