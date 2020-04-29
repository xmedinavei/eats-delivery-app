"""Order serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from orders.models import Order


class OrderModelSerializer(serializers.ModelSerializer):
    '''Order model serializer.'''

    # user = UserModelSerializer()
    # customer = CustomerModelSerializer()
    # store = StoreModelserializer()

    class Meta:
        """Meta class."""

        model = Order
        fields = (
            'user',
            'customer',
            'store',
            'paid',
            'picked_up',
            'deliveried',
            'created',
            'updated'
        )
        read_only_fields = (
            'created',
            'updated'
        )