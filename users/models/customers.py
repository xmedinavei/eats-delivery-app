'''Customer model.'''

# Django
from django.db import models

# Models
from .users import User


class Customer(models.Model):
    '''Customer model.

    Customer profile hold user's public data: picture and stats.
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=True)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/customers/pictures/',
        blank=True,
        null=True
    )

    delivery_address = models.CharField(max_length=250)

    # Stats
    orders_made = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ['-id']


    def __str__(self):
        '''Return user's str representation.'''
        return str(self.user)

