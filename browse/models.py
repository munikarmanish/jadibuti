from django.db import models
from django.core.urlresolvers import reverse 

# Create your models here.

class HerbCategory (models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return name


class Herb(models.Model):
    sci_name = models.CharField(max_length=50, null=True)
    eng_name = models.CharField(max_length=50)
    nep_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(
        null=True, blank=True,
        width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description = models.TextField ()

    category = models.ManyToManyField (HerbCategory)

    def get_absolute_url (self):
        #return '#'
    	return reverse('browse:herb', kwargs={'slug': self.id})


class Disease(models.Model):
    name = models.CharField(max_length=255)


class CarouselImage (models.Model):
    show = models.BooleanField (null=False, default=True)

    image = models.ImageField (null=False, blank=False, 
        width_field='width_field', height_field='height_field')

    height_field = models.IntegerField (default=0)
    width_field = models.IntegerField (default=0)

    caption = models.CharField (max_length=100)

    description = models.CharField (max_length=255)

