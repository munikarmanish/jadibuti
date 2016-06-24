from django import models


class Disease(models.Model):
    name = models.CharField(max_length=255)


class CarouselImages (models.Model):
	image = models.ImageField (null=False, blank=False, 
		width_field='width_field', height_field='height_field')
	height_field = models.IntegerField (default=0)
	width_field = models.IntegerField (default=0)

	caption = models.CharField (max_length=100)

	desctiption = models.CharField (max_length=255)

	