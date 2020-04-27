"""Rider serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from users.models import Rider


class RiderModelSerializer(serializers.ModelSerializer):
    '''Rider model serializer.'''


    class Meta:
        """Meta class."""

        model = Rider
        fields = (
            'first_name',
            'last_name',
            'picture',
            'vehicle_made',
            'vehicle_model',
            'licence_plate',
            'rider_address',
            'orders_dispatched',
            'reputation'
        )
        read_only_fields = (
            'orders_dispatched',
            'reputation'
        )
