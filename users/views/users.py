'''Users views.'''

# Django REST Framework
from rest_framework.views import APIView
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

# Serializers
from users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer,
    CustomerModelSerializer,
)

from users.permissions import IsAccountOwner

# Models
from users.models import User, Customer



class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """User view set.

    For sign up, login and account verification.
    """

    queryset = User.objects.filter(is_verified=True, type_user='customer')
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]  # No pide permisos
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""

        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        
        return Response(data, status=status.HTTP_201_CREATED)
        
        
    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account verification."""

        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Your account is already verified!'}

        return Response(data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['put', 'patch'])
    def customer(self, request, *args, **kwargs):
        """Update customer data."""
        user = self.get_object()
        customer = user.customer
        partial = request.method == 'PATCH'
        serializer = CustomerModelSerializer(
            customer,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)

    # Show user orders 
    # def retrieve(self, request, *args, **kwargs):
    #     """Add extra data to the response."""

    #     response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
    #     order_active = Orders.objects.filter(
    #         owner=request.user,
    #         order__is_deliveried=True
    #     )
    #     order_made= Orders.objects.filter(
    #         owner=request.user,
    #         order__is_deliveried=False
    #     )
    #     data = {
    #         'user': response.data,
    #         'order_active': OrderModelSerializer(order_active, many=True).data,
    #         'order_made': OrderModelSerializer(order_made, many=True).data
    #     }
    #     response.data = data
    #     return response
