"""Meal serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from meals.models import Meal

# Serializers
from users.serializers import StoreModelSerializer


class MealModelSerializer(serializers.ModelSerializer):
    '''Meal model serializer.'''

    # store = StoreModelSerializer()

    class Meta:
        """Meta class."""

        model = Meal
        fields = (
            'store',
            'name',
            'slugname',
            'description',
            'price',
            'picture',
            'rating'
        )
        read_only_fields = (
            'rating',
        )
