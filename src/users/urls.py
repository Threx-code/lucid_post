from django.http import HttpResponse
from django.urls import path, include
from knox import views as knox_views
from helpers import fields as input_fields
from . import views

app_name = "user"

urlpatterns = [
    path("", lambda request: HttpResponse("Hello, thank you for visiting the user app"), name=input_fields.USER),
    path("signup/", views.UserRegistrationAPI.as_view(), name=input_fields.SIGNUP)
]