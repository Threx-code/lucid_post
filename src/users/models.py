import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from .manager.user_manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email= models.EmailField(max_length=255, unique=True, null=False, db_index=True)
    password= models.CharField(max_length=255, null=False)
    is_active= models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_user_group',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='user',
    )


    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
