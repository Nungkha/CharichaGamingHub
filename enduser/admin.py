from django.contrib import admin
from .models import CustomUser, Profile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','email','user_type', 'joined_at']
    list_filter = ['username', 'email', 'user_type']
    search_fields = ['username', 'email']
    fieldsets = (
        (None, {"fields": ("email", "password","username","user_type")}),
        ("Permissions", {"fields": ("is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email","username","user_type", "password1", "password2", 
                "is_active", "groups", "user_permissions"
            )}
        ),
    )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'user_type', 'created_at', 'image']
    list_filter = ['user', 'first_name', 'last_name', 'user_type']
    search_fields = ['user', 'first_name', 'last_name']
    fieldsets = (
        (None, {
            "fields": (
                "user", "user_type", "first_name", "last_name", "bio", "image", "cover_photo",
            ),
        }),
    )
    



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
