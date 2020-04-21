'''User model.'''

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



class User(AbstractUser):
    '''User model which extends from Django Abstract User.
    User will be related by proxy model to: [client, seller or driver]

    The username field has been changed to email.
    '''

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    # Regex validator for phone_number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{10,12}$',
        message="Phone number must be entered in the format: +593987654321 or 0987654321. Up to 12 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=13,
    )

    # Kind of user
    CUSTOMER = 'CU'
    STORE = 'ST'
    RIDER = 'RD'
    ADMIN = 'AD'
    TYPE_USER_CHOICES = [
        (CUSTOMER, 'customer'),
        (STORE, 'store'),
        (RIDER, 'rider'),
        (ADMIN, 'admin'),
    ]
    type_user = models.CharField(
        max_length=2,
        choices=TYPE_USER_CHOICES,
        default=CUSTOMER,
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']


    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )

    def __str__(self):
        '''Return username.'''
        return self.username

    # Method in Abstract User
    def get_short_name(self):
        '''Return username.'''
        return self.first_name
