from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields": ("username", "password")}),
        ("개인정보", {"fields": ("first_name", "last_name", "email")}),
        ("추가정보", {"fields": ("profile_image", "short_description")}),
        ("권한", {"fields": ("is_active", "is_staff", "is_superuser",)}),
        ("info", {"fields": ("last_login", "date_joined")}),
    ]
    pass
