'''Users serializers.'''

# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models import User, Customer

# Utilities
import jwt
from datetime import timedelta


class UserModelSerializer(serializers.ModelSerializer):
    '''User model serializer.'''

    class Meta:
        '''Meta class.'''

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )
        # fields = '__all__'



class UserSignUpSerializer(serializers.Serializer):
    '''User signup serializer.
    
    Handle sign up data validation and customer creation
    '''

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

   
    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{10,12}$',
        message="Phone number must be entered in the format: +593987654321 or 0987654321. Up to 12 digits allowed."
    )
    phone_number = serializers.CharField(
        validators=[phone_regex], max_length=13,
    )

    # passwrod
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)
   
    # Type of user
    CUSTOMER = 'CU'
    STORE = 'ST'
    RIDER = 'RI'
    ADMIN = 'AD'
    TYPE_USER_CHOICES = [
        (CUSTOMER, 'customer'),
        (STORE, 'store'),
        (RIDER, 'rider'),
        (ADMIN, 'admin'),
    ]
    type_user = serializers.ChoiceField(choices=TYPE_USER_CHOICES, default=CUSTOMER,)


    def validate(self, data):
        '''Verify that passwords match'''

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match.')
        
        # Django's validation
        password_validation.validate_password(password)
        return data


    def create(self, data):
        '''handle user and customer creation.'''

        data.pop('password_confirmation')
        user = User.objects.create(**data, is_verified=False)
        Customer.objects.create(user=user)

        self.send_confirmation_email(user)
        return user


    def send_confirmation_email(self, user):
        '''Send verification email to make user's account is_verfied=True'''

        verification_token = self.gen_verification_token(user)

        subject = f'Welcome @{user.username}! Verify you account'
        from_email = 'Eats Delivery <noreply@eatsdelivery.com>'
        to = user.email
        content = render_to_string(
            'emails/account_verification.html',
            {'token': verification_token, 'user': user}
        )

        msg = EmailMultiAlternatives(subject, content, from_email, [to])
        msg.attach_alternative(content, "text/html")
        msg.send()


    def gen_verification_token(self, user):
        '''Create JWT for the user, to verify the account.'''

        exp_date = timezone.now() + timedelta(days=3)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token.decode()




class UserLoginSerializer(serializers.Serializer):
    '''User login serializer.'''

    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8,
        max_length=64
        )

    def validate(self, data):
        '''Verify credentials.'''
        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Invalid credentials.')

        if not user.is_verified:
            raise serializers.ValidationError('User has not been verified')

        self.context['user'] = user
        return data

    def create(self, data):
        '''Generate or retrieve token.'''
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class AccountVerificationSerializer(serializers.Serializer):
    '''Account verification token serializer.'''

    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY,
                                 algorithms=['HS256'])
        # Validate that token has not been expired
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        # Validate that we are receiving a token, not other string
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        # Validate that email was send by Eats App
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token')

        self.context['payload'] = payload
        return data


    def save(self):
        """Update user to is_verified=True"""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()





