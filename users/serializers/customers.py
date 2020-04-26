"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from users.models import Customer


class CustomerModelSerializer(serializers.ModelSerializer):
    """Customer model serializer."""

    class Meta:
        """Meta class."""

        model = Customer
        fields = (
            'picture',
            'delivery_address',
            'is_customer',
            'orders_made'
        )
        read_only_fields = (
            'is_customer',
            'orders_made'
        )
