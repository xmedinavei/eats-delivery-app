'''Order items views.'''

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Serializers
from orders.serializers import OrderItemModelSerializer

#  Models
from orders.models import Order
from users.models import User
from users.models import Customer
from users.models import Store
from meals.models import Meal



class OrderItemViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    '''Order item view set.
    
    #####################################################################################################################################
    Http methods and the URLs:

    POST        users/<username>/stores/<store_slugname>/orders/<uid>/meal/<slugname>/       (Insert Meal into an existing User's Order )
    #####################################################################################################################################
    '''

    serializer_class = OrderItemModelSerializer
    lookup_field = 'id'
    search_fields = ('id', 'meal.name')


    # Method call every time this MealViewSet is instanced
    def dispatch(self, request, *args, **kwargs):
        '''Add the username, store, order and meal to the attributes.
        Got from the URL input.
        '''

        username = kwargs['username']
        store_slugname = kwargs['store_slugname']
        uid = kwargs['uid']
        slugname = kwargs['slugname']
        self.user = get_object_or_404(User, username=username)
        self.store = get_object_or_404(Store, store_slugname=store_slugname)
        self.order = get_object_or_404(Order, id=uid)
        self.meal = get_object_or_404(Meal, slugname=slugname)

        return super(OrderItemViewSet, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        '''Get User's Order'''
        # MODIFY LSIT AND DELETE 

        return Order.objects.filter(
            id=self.order.id,
            user=self.user.id,
            store=self.store.id,
            ordered=False
        )

    def create(self, request, *args, **kwargs):
        '''Add an order_item (meal) of an Order.'''

        request.data['order'] = self.order.id
        request.data['meal'] = self.meal.id

        serializer = OrderItemModelSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)