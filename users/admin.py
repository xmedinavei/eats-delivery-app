"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import User, Customer, Rider, Store


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('id','email','password', 'username', 'first_name',
                    'last_name', 'type_user', 'is_verified', 'type_user', 'is_active')
    list_filter = ('is_verified', 'type_user', 'is_active')
    ordering = ['-id']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer model admin."""

    list_display = ('id', 'user', 'delivery_address', 'orders_made')
    search_fields = (
        'user__username', 'user__email',
        'user__first_name', 'user__last_name'
    )
    ordering = ['-id']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Store model admin."""

    list_display = (
        'id', 'name', 'store_slugname', 'pickup_address',
        'is_active', 'is_open',
        'orders_dispatched', 'reputation'
    )
    list_filter = ('is_active','is_open')
    search_fields = ('id', 'name', 'store_slugname')
    ordering = ['-id']


@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    """Rider model admin."""

    list_display = (
        'id', 'first_name', 'last_name', 'location',
        'orders_dispatched','reputation', 'vehicle_made',
        'vehicle_model', 'licence_plate', 'orders_active', 'is_available',
        'is_active', 'orders_dispatched', 'reputation'
    )
    search_fields = ('id', 'first_name', 'last_name', 'licence_plate')
    list_filter = ('orders_active', 'is_active', 'is_available')
    ordering = ['-id']


admin.site.register(User, CustomUserAdmin)
