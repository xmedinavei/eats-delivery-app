"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import User, Customer, Rider, Store


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('id','email', 'username', 'password', 'first_name',
                    'last_name', 'type_user')
    list_filter = ('is_verified', 'type_user')

    ordering = ['-id']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer model admin."""

    list_display = ('id', 'user', 'delivery_address', 'orders_made')
    search_fields = ('user__username', 'user__email',
                     'user__first_name', 'user__last_name')
    # list_filter = ('',)

    ordering = ['-id']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Store model admin."""

    list_display = (
        'id', 'name', 'slugname', 'pickup_address',
        'orders_dispatched', 'reputation'
    )
    # search_fields = (
    #     'user__username', 'user__email',
    #     'user__first_name', 'user__last_name',
    #     'name', 'slugname',
    # )
    # list_filter = ('',)

    search_fields = ('name', 'slugname')

    ordering = ['-id']


@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    """Rider model admin."""

    list_display = (
        'id', 'first_name', 'last_name', 'rider_address',
        'orders_dispatched','reputation', 'vehicle_made',
        'vehicle_model', 'licence_plate', 'available', 'active'
    )
    # search_fields = (
    #     'user__username', 'user__email',
    #     'user__first_name', 'user__last_name',
    #     'licence_plate',
    # )
    search_fields = ('first_name', 'last_name', 'licence_plate')

    list_filter = ('available',)

    ordering = ['-id']

admin.site.register(User, CustomUserAdmin)
