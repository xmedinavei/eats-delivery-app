'''Stores views.'''

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Serializers
from users.serializers import StoreModelSerializer
from orders.serializers import OrderModelSerializer

# Models
from users.models import Store
from orders.models import Order

class StoreViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    '''Stores view set.
    
    #################################################################################
    Http methods and the URLs:

    GET             /stores/                        (list Stores)
    POST            /stores/                        (create Store)
    PUT             /stores/                        (update Store info)
    PATCH           /stores/                        (partial update Store info
    GET            /stores/<id>/orders/            (show Orders not pickup yet)
    ######################################################################################
    '''

    serializer_class = StoreModelSerializer
    lookup_field = 'store_slugname'

    search_fields = ('store_slugname', 'name')
    # It will be implemented
    # ordering = () # Ordering by distance to customer
    filter_fields = ('is_active', 'is_open')

    def get_queryset(self):
        '''Get only open and active Stores.'''

        queryset = Store.objects.all()
        if self.action == 'list':
            queryset = (
                    queryset
                    .filter(is_open=True)
                    .filter(is_active=True)
            )
            return queryset
            
        return queryset

    
    @action(detail=True, methods=['GET'])
    def orders(self, request, *args, **kwargs):
        '''Show orders assign to the Rider.'''
        # import pdb; pdb.set_trace()
        store = get_object_or_404(Store, store_slugname=kwargs['store_slugname'])
        orders_assigned = (
            store.order_set.all()
                .filter(picked_up=False)
                .filter(deliveried=False)
        ) 
        n = len(orders_assigned)
        for i in range(n):
            data = OrderModelSerializer(orders_assigned[i]).data

        return Response(data, status=status.HTTP_200_OK)
    
