"""Store serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from users.models import Store


class StoreModelSerializer(serializers.ModelSerializer):
    '''Store model serializer.'''


    class Meta:
        """Meta class."""

        model = Store
        fields = (
            'name',
            'store_slugname',
            'about',
            'picture',
            'pickup_address',
            'orders_dispatched',
            'reputation'
        )
        read_only_fields = (
            'orders_dispatched',
            'reputation'
        )
