'''Order views.'''

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Serializers
from order.serializers import OrderModelSerializer

#  Models
from orders.models import Order
from users.models import User
from users.models import Customer
from users.models import Store



# class MealViewSet(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.DestroyModelMixin,
#                     viewsets.GenericViewSet):
#     '''Meals view set.
    
#     #################################################################################
#     Http methods and the URLs:

#     GET             /users/(<username>/customer/orders/         (list )
#     POST            /users/(<username>/customer/orders          (create)
#     ######################################################################################
#     '''

#     serializer_class = Order
#     lookup_field = 'id'
#     search_fields = ('id', 'user__username')


#     # Method call every time this MealViewSet is instanced
#     def dispatch(self, request, *args, **kwargs):
#         '''Add the use and customer to the attributes.'''


#         username = kwargs['store_slugname']
#         self.store = get_object_or_404(Store, store_slugname=store_slugname)

#         return super(MealViewSet, self).dispatch(request, *args, **kwargs)


#     def get_queryset(self):
#         '''Get Store's available meals'''

#         return Meal.objects.filter(
#             store=self.store,
#             is_available=True
#         )
    
#     def create(self, request, *args, **kwargs):
#         '''Assign Meal to a Store (received in the URL input <store_slugname>)
#         '''
#         store = self.store # Got from the dispatcher
#         request.data['store'] = store.id
#         serializer = MealModelSerializer(
#             data=request.data
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = serializer.data

#         return Response(data, status=status.HTTP_201_CREATED)