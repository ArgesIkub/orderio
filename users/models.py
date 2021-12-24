from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING

class UserRole(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):

    user_role = models.ForeignKey(UserRole, on_delete=DO_NOTHING, blank=True, null=True)
