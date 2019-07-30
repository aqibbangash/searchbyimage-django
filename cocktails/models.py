from __future__ import unicode_literals

from django.db import models



# Create your models here.

class Cocktails(models.Model):
    name = models.TextField()
    # Example:
    #  "{\"Dry Vermouth\": \"1 part\", \"Vodka\": \"2 parts\", \"Garnish\": \"one lemon twist\", \"Orange Bitters\": \"one dash\"}"

    ingredients = models.TextField()
    directions = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.name


class Inventory(models.Model):
    image = models.FileField(null=True, blank=True)
    prediction = models.TextField()









# use json.loads to bring out json from db

