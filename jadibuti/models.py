from django import models


class Herb(models.Model):
    sci_name = models.CharField(max_length=50, null=True)
    eng_name = models.CharField(max_length=50)
    nep_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(
        null=True, blank=True,
        width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)


class Disease(models.Model):
    name = models.CharField(max_length=255)

class Categories(models.Model):
    name = models.CharField(max_length=255)
