'''Restaurant's meal models.'''

# Django
from django.db import models

# Local
from eatsapp_project.users.models import Store

class Meal(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    meal_name = models.CharField()
    price = models.DecimalField(
        'meal price',
        max_digits=5,
        decimal_places=2
        )
    picture = models.ImageField(
        'meal picture',
        upload_to='meals/pictures/',
        blank=True,
        null=True,
        help_text="Price max up to $999.99"
    )
    meal_rating = models.FloatField(
        default=5.0,
        help_text="Meal's rating based on client califications"
    )
