"""Order iterms serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from orders.models import OrderItem


class OrderItemModelSerializer(serializers.ModelSerializer):
    '''Order items model serializer.'''

    class Meta:
        """Meta class."""

        model = OrderItem
        fields = (
            'order',
            'meal',
            'quantity'
        )
        # read_only_fields = ()
