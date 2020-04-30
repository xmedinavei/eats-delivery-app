'''Riders views.'''

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


# Serializers
from users.serializers import RiderModelSerializer
from orders.serializers import OrderModelSerializer

# Models
from users.models import Rider

class RiderViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    '''Riders view set.
    
    #################################################################################
    Http methods and the URLs:

    GET             /riders/                        (list Riders)
    POST            /riders/                        (create Rider)
    PUT             /riders/                        (update Rider info)
    PATCH           /riders/                        (partial Rider Store info)
    GET             /riders/<id>/orders/            (show orders to pickup)
    ######################################################################################
    '''

    serializer_class = RiderModelSerializer
    lookup_field = 'slugname'

    search_fields = (
            'first_name',
            'last_slugname',
            'vehicle_made',
            'vehicle_model',
            'licence_plate',
            'rider_address'
        )
    # It will be implemented
    # ordering = () # Ordering by distance to customer
    filter_fields = ('is_active', 'is_available')

    def get_queryset(self):
        '''Get only active and available Riders.'''

        queryset = Rider.objects.all()
        if self.action == 'list':
            queryset = (
                    queryset
                    .filter(is_available=True)
                    .filter(is_active=True)
            )
            return queryset
            
        return queryset
    

    @action(detail=True, methods=['GET'])
    def orders(self, request, *args, **kwargs):
        '''Show orders assign to the Rider.'''
        rider = get_object_or_404(Rider, id=kwargs['slugname']) # Don't know why appears slugnmame in kwargs. There's no slugname in models even
        orders_assigned = (
            rider.order_set.all()
                .filter(picked_up=False)
                .filter(deliveried=False)
        ) 
        # import pdb; pdb.set_trace()
        n = len(orders_assigned)
        for i in range(n):
            data = OrderModelSerializer(orders_assigned[i]).data

        return Response(data, status=status.HTTP_200_OK)