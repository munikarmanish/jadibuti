from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from time import time


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    image = models.ImageField(
        null=True, blank=True,
        width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    tags = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})


def create_slug(instance):
    time_str = "".join(str(time()).split('.'))
    slug_string = "%s-%s" % (instance.title, time_str[5:])
    instance.slug = slugify(slug_string)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)

