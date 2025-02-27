from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from .repositories.post_repository import PostRepository
from .serializers.serializer import PostSerializer
from .services.post_service import PostService


class AddPostView(generics.GenericAPIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    post_service = PostService(PostRepository())  # Dependency Injection

    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        post_id = self.post_service.create(request.user, text)
        return Response({"post_id": post_id}, status=status.HTTP_201_CREATED)


class GetPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    post_service = PostService(PostRepository())  # Dependency Injection

    def get_queryset(self):
        return self.post_service.get_posts(self.request.user)


class DeletePostView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    post_service = PostService(PostRepository())  # Dependency Injection

    def delete(self, request, *args, **kwargs):
        post_id = request.data.get("post_id")
        self.post_service.delete_post(request.user, post_id)
        return Response({"message": "Post deleted"}, status=status.HTTP_204_NO_CONTENT)
