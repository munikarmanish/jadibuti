from django.db import models

# Create your models here.

class HerbCategory (models.Model):
    name = models.CharField(max_length=50, null=False)

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
    	return reverse('browse:browse', kwargs={'slug': self.sci_name})

