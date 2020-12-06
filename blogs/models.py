from django.db import models
import os
import random
from django.db import models
from django.db.models import Count
from django.conf import settings
from django.utils import timezone

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename= random.randint(1, 9999999999)
    name, ext = get_filename_ext(filename)
    print(name, ext)
    final_converted_name = "{new_filename}{ext}".format(
        new_filename=new_filename, ext=ext
    )
    print("final function")
    print(final_converted_name)
    print("articles/{new_filename}/{final_converted_name}".format(
        new_filename=new_filename, final_converted_name=final_converted_name
    ))
    return "articles/{new_filename}/{final_converted_name}".format(
        new_filename=new_filename, final_converted_name=final_converted_name
    )

class CustomArticleQuerySet(models.query.QuerySet):
    def get_new(self):
        return self.filter(new=True).order_by('id')[:6]


class ArticlesManager(models.Manager):
    def get_queryset(self):
        return CustomArticleQuerySet(self.model, using=self._db)

    def get_new(self):
        return self.get_queryset().get_new()

class Articles(models.Model):
    title = models.CharField(max_length=120)
    content  = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    KG = 'KG'
    WORLD = 'WORLD'
    SPORT = 'SPORT'
    CATEGORY_OF_ARTICLES = (
        (KG, 'KG'),
        (WORLD, 'WORLD'),
        (SPORT, 'SPORT'),
    )
    article_category = models.CharField(
        max_length=15,
        choices=CATEGORY_OF_ARTICLES,
        default=KG, 
        null=True, 
        blank=True
        )

    objects = ArticlesManager()
    image = models.ImageField(
        upload_to=upload_image_path, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f"{self.title} -> {self.article_category}"
    
    class Meta:
        ordering = ['-created_date']

