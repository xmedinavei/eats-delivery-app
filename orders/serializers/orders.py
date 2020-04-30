"""Order serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from orders.models import Order, OrderItem


class OrderModelSerializer(serializers.ModelSerializer):
    '''Order model serializer.'''

    class Meta:
        """Meta class."""

        model = Order
        fields = (
            'id',
            'user',
            'customer',
            'store',
            'rider',
            'paid',
            'ordered',
            'picked_up',
            'deliveried',
            'created',
            'updated'
        )
        read_only_fields = (
            'created',
            'updated'
        )