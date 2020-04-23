'''Rider model.'''

# Django
from django.db import models
from django.core.validators import RegexValidator

# Models
from .users import User


class Rider(models.Model):
    '''Rider model.

    Rider profile hold user's public data: picture and stats.
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/riders/pictures/',
        blank=True,
        null=True
    )

    # Motorcicle
    vehicle_made = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    # Regex validator for motorcicle licence plate
    licence_plate_regex = RegexValidator(
        regex=r'^\w{2}\d{3}\w$',
        message="Motorcicle  licence plate must be entered in the format: AA111A"
    )
    licence_plate = models.CharField(
        validators=[licence_plate_regex], max_length=6,
        unique=True,
    )

    rider_address = models.TextField(max_length=200, blank=True)

    # Status
    available = models.BooleanField(
        'is the rider available to deliver?',
        default=True
    )
    active = models.BooleanField(
        'is an active',
        default=True
    )
    # Stats
    orders_dispatched = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="Rider's reputation based on client califications"
    )


    class Meta:
        ordering = ['-id']


    def __str__(self):
        '''Return user's str representation.'''
        return str(self.user)
