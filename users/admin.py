from django.contrib import admin
from users.models import CustomUser, UserRole

# Register your models here.
admin.site.register(UserRole)
admin.site.register(CustomUser)
