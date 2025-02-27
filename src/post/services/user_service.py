from ..interfaces.user_interface import UserRepositoryInterface

class UserService:

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository


    def create(self, email: str, password: str):
        return self.repository.create(email, password)


    def get_all(self):
        return self.repository.get_all()


    def email_exists(self, email: str) -> bool:
        return self.repository.email_exists(email)
