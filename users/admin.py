"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name',
                    'last_name', 'type_user')
    list_filter = ('is_client', 'type_user')


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     """Customer model admin."""

#     list_display = ('user', 'reputation', 'rides_taken', 'rides_offered')
#     search_fields = ('user__username', 'user__email',
#                      'user__first_name', 'user__last_name')
#     list_filter = ('reputation',)


# admin.site.register(User, CustomUserAdmin)
