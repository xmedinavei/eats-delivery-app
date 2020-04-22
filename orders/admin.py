"""Meals models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order model admin."""

    list_display = (
        'customer', 'paid', 'picked_up', 'deliveried'
    )
    search_fields = (
        'id',
    )
    list_filter = ('paid', 'picked_up', 'deliveried')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Order item model admin."""

    list_display = (
        'order', 'meal', 'quantity'
    )
    search_fields = (
        'order', 'id',
    )
