from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.

class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, null=True, default=None, verbose_name="Category",
                                          on_delete=models.CASCADE)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    tutorial_series = models.ForeignKey(TutorialSeries, null=True, default=None, verbose_name="Series",
                                          on_delete=models.CASCADE)
    tutorial_slug = models.CharField(max_length=200, default=1)
    tutorial_image = models.ImageField(upload_to='main/img', blank=True)
    def __str__(self):
        return self.tutorial_title




class Account(models.Model):
    tutorial_category = models.CharField(max_length=200)
