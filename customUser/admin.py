from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    list_display = ('username',)
    search_fields = ['email']

class UserAdmin(BaseUserAdmin):
    inlines = (CustomUserInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
