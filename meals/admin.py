"""Meals models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from meals.models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """Meal model admin."""

    list_display = (
        'store', 'name', 'slugname', 'price', 'rating'
    )
    search_fields = (
        'slugname', 'slugname',
                     )

