from django.db import models


class Location(models.Model):
    """Model representation of a location. Fields include city_name and one-to-many relationship with Item"""
    city_name = models.CharField('name of city', max_length=50)

    def __str__(self):
        return self.city_name


class Item(models.Model):
    """Model representation of an item. Fields include name, description and count"""
    count = models.IntegerField('number of items in inventory', default=1)
    name = models.CharField('name of item', max_length=50)
    description = models.CharField('description of item', max_length=200, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def has_description(self):
        """Returns True if item has a description"""
        return self.description != ""

    def __str__(self):
        return self.name
