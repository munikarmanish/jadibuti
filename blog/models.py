from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from time import time
from browse.models import *


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
    categories = models.ManyToManyField(Category,blank=True)
    herbs = models.ManyToManyField(Herb,blank=True)

    yogas = models.ManyToManyField (Yoga,blank=True)
    diseases = models.ManyToManyField (Disease,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def reviews(self):
        return self.review_set.all().order_by('-created')

    def rating(self):
        r = 0
        reviews = self.reviews()

        if reviews:
            for review in reviews:
                r += review.star
            return r / len(reviews)
        else:
            return None


def create_slug(instance):
    time_str = "".join(str(time()).split('.'))
    slug_string = "%s-%s" % (instance.title, time_str[5:])
    instance.slug = slugify(slug_string)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)


STAR_CHOICES = (
    (1, '1 Star'),
    (2, '2 Star'),
    (3, '3 Star'),
    (4, '4 Star'),
    (5, '5 Star'),
)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    star = models.SmallIntegerField(choices=STAR_CHOICES, default=3)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        if len(self.comment) <= 30:
            return self.comment
        else:
            return self.comment[0:27] + '...'
