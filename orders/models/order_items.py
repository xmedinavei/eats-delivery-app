'''Order items models.'''

# Django
from django.db import models

# Models
from users.models import User, Customer, Store
from meals.models import Meal
from orders.models import Order


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'Order Item id: {} name: {}'.format(
            self.id,
            self.meal.name
        )

    # def get_cost(self):
    #     return self.Meal.price * self.quantity
