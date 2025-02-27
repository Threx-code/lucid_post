from asgiref.timeout import timeout
from django.core.cache import cache
from ..interfaces.post_interface import PostRepositoryInterface
from ..models import Post

class UserRepository(PostRepositoryInterface):

    def __init__(self):
        self.post = Post


    def create(self, user, text):
        post = self.post.objects.create_user(
            user=user,
            text=text
        )

        return post


    def get_all(self):
        return self.post.objects.all()

    def get_post(self, user):
        cache_key = f'posts_{user.id}'
        posts = cache.get(cache_key)
        if not posts:
            posts = self.post.objects.filter(user=user)
            cache.set(cache_key, posts, timeout=300)

        return posts


    def delete_post(self, user, post_id):
        self.post.filter(user=user, id=post_id).delete()

