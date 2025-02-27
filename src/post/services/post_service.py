from ..interfaces.post_interface import PostRepositoryInterface

class PostService:

    def __init__(self, repository: PostRepositoryInterface):
        self.repository = repository

    def create(self, email: str, password: str):
        return self.repository.create(email, password)

    def get_all(self):
        return self.repository.get_all()

    def get_posts(self, user):
        return self.repository.get_post(user)

    def delete_post(self, user, post_id):
        return self.repository.delete_post(user, post_id)



