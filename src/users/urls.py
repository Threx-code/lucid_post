from django.http import HttpResponse
from django.urls import path, include
from knox import views as knox_views
from . import views

app_name = "user"

urlpatterns = [
    path("", lambda request: HttpResponse("Hello, thank you for visiting the user app"), name="index"),
    path("signup/", views.UserRegistrationAPI.as_view(), name="signup")
]