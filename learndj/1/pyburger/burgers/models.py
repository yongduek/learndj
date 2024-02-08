from django.db import models

# Create your models here.

class Burger(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.name