# '''Order items views.'''

# # Django REST Framework
# from rest_framework import mixins, status, viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.generics import get_object_or_404

# # Serializers
# from order.serializers import OrderItemModelSerializer

# #  Models
# from orders.models import Order
# from users.models import User
# from users.models import Customer
# from users.models import Store
# from meals.models import Meal



# class OrderItemViewSet(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.DestroyModelMixin,
#                     viewsets.GenericViewSet):
#     '''Order item view set.
    
#     #################################################################################
#     Http methods and the URLs:

#     GET             /users/(<username>/customer/orders/         (list )
#     POST            /users/(<username>/customer/orders          (create)
#     ######################################################################################
#     '''

#     serializer_class = OrderItemModelSerializer
#     lookup_field = 'id'
#     search_fields = ('id', 'meal.name')


#     # Method call every time this MealViewSet is instanced
#     def dispatch(self, request, *args, **kwargs):
#         '''Add the username, store and meal to the attributes.
#         Got from the URL input.
#         '''

#         username = kwargs['username']
#         store_slugname = kwargs['store_slugname']
#         slugname = kwargs['slugname']
#         self.username = get_object_or_404(User, username=username)
#         self.store = get_object_or_404(Store, store_slugname=store_slugname)
#         self.meal = get_object_or_404(Meal, slugname=slugname)

#         return super(OrderItemViewSet, self).dispatch(request, *args, **kwargs)


#     def get_queryset(self):
#         '''Get Store's available meals'''

#         return Meal.objects.filter(
#             store=self.store,
#             slugname=self.meal.slugname
#             is_available=True
#         )
    
    # def perform_create(self, serializer):
    #     '''Create an order item of an order.'''







    # def create(self, request, *args, **kwargs):
    #     store = self.store # Got from the dispatcher
    #     request.data['store'] = store.id
    #     serializer = OrderItemModelSerializer(
    #         data=request.data
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     data = serializer.data

    #     return Response(data, status=status.HTTP_201_CREATED)