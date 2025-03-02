from django.urls import path

from . import views


app_name = "post"

urlpatterns = [
path("add_post/", views.AddPostView.as_view(), name="add_post"),
    path("get_posts/", views.GetPostsView.as_view(), name="get_posts"),
    path("delete_post/", views.DeletePostView.as_view(), name="delete_post"),
]