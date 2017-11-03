from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User


class UserAdmin(BaseUserAdmin):
    add_fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )


admin.site.register(User, UserAdmin)
