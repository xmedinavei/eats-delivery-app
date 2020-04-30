'''Order views.'''

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Serializers
from orders.serializers import OrderModelSerializer

#  Models
from orders.models import Order
from users.models import User, Customer, Store, Rider



class OrderViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    '''Order view set.
    
    ############################################################################################################################
    Http methods and the URLs:

    GET         /users/<username>/stores/<store_slugname>/orders/                   (list Customer's order from a Store)
    POST        /users/<username>/stores/<store_slugname>/orders/                   (create) # DO NOT SEND DATA TO CREATE AN ORDER
    POST        /users/<username>/stores/<store_slugname>/orders/<id>/make_order/   (make order and assign a Rider)
    #############################################################################################################################
    '''

    serializer_class = OrderModelSerializer
    lookup_field = 'id'
    search_fields = ('id', 'user__username', 'store__store_slugname')


    def dispatch(self, request, *args, **kwargs):
        '''Add the username, store and meal to the attributes.
        Got from the URL input.
        '''

        username = kwargs['username']
        store_slugname = kwargs['store_slugname']
        self.user = get_object_or_404(User, username=username)
        self.store = get_object_or_404(Store, store_slugname=store_slugname)

        return super(OrderViewSet, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        '''Get Store's available meals'''

        return Order.objects.filter(
            user=self.user.id,
            store=self.store.id
        )

    def get_object(self):
        """Return the Order objects from get_queryset."""
        return get_object_or_404(
            Order,
            user=self.user.id,
            store=self.store.id
        )

    def create(self, request, *args, **kwargs):
        '''Create an order.'''

        request.data['user'] = self.user.id
        request.data['customer'] = self.user.customer.id
        request.data['store'] = self.store.id

        serializer = OrderModelSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['POST'])
    def make_order(self, request, *args, **kwargs):
        
        order = get_object_or_404(
            Order,
            id=kwargs['id'],
            user=self.user.id,
            store=self.store.id
        )

        # Assign Rider
        query_riders = Rider.objects.filter(is_active=True).filter(is_available=True)
        rider_available = query_riders.first()
        rider_id = rider_available.id
        rider_instance = Rider.objects.get(id=rider_id)

        # Order: Add Rider and set ordered=True
        order.rider = rider_instance
        order.ordered = True
        data = OrderModelSerializer(order).data

        return Response(data, status=status.HTTP_200_OK)