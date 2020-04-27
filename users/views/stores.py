'''Stores views.'''

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from users.serializers import StoreModelSerializer

# Models
from users.models import Store

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
    PATCH           /stores/                        (partial update Store info)
    ######################################################################################
    '''

    serializer_class = StoreModelSerializer
    lookup_field = 'slugname'

    search_fields = ('slug_name', 'name')
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
    
