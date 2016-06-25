from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class HerbCategory (models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class HerbShop (models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=250, null=False, blank=False)

    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

    #herbs = models.ManyToManyField (Herb)

    def __str__():
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=255)

class Herb(models.Model):
    sci_name = models.CharField(max_length=50, null=True, blank=True)
    eng_name = models.CharField(max_length=50)
    nep_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True,
        width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    categories = models.ManyToManyField(HerbCategory)

    shops = models.ManyToManyField(HerbShop, blank=True)

    curable_diseases = models.ManyToManyField(Disease, blank=True)

    def get_absolute_url(self):
        return reverse('browse:herb', kwargs={'slug': self.id})

    def __str__(self):
        return self.eng_name

class CarouselImage (models.Model):
    show = models.BooleanField(null=False, default=True)

    image = models.ImageField(
        null=False, blank=False,
        width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    caption = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.caption
