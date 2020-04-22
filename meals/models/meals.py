'''Restaurant's meal models.'''

# Django
from django.db import models

# Models
from users.models import Store

class Meal(models.Model):
    '''Meals models.'''

    store = models.ForeignKey(
        Store, 
        on_delete=models.CASCADE,
        )
    
    name = models.CharField(max_length=120)
    slugname = models.SlugField(
        unique=True,
        max_length=120,
        )
    description = models.TextField(max_length=300, blank=True)
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

    # Stats
    rating = models.FloatField(
        default=5.0,
        help_text="Meal's rating based on client califications"
    )
    
    
    class Meta:
        ordering = ('slugname', )
        verbose_name = 'meal'

    def __str__(self):
        return 'Meal  {}'.format(self.slugname)

