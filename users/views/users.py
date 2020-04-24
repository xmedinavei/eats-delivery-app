'''Users views.'''

# Django REST Framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Serializers
from users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer,
)


class UserLoginAPIView(APIView):
    '''User login API View.'''

    def post(self, request, *args, **kwargs):
        '''Handle HTTP POST request.'''
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    '''User signup API View.'''

    def post(self, request, *args, **kwargs):
        '''Handle HTTP POST request.'''
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class AccountVerificationAPIView(APIView):
    '''Verify the token sent to email(by console) to confirm an account.'''

    def post(self, request, *args, **kwargs):
        '''Handle HTTP POST request.'''
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Your account is already verified!'}
        return Response(data, status=status.HTTP_200_OK)
