from django.db import models
from django.urls import reverse
from oxcimarron.utils import Utils

# Create your models here.


class Author(models.Model):
    last_name = models.CharField(max_length=60, null=False, blank=False)
    first_name = models.CharField(max_length=60, null=True, blank=True)
    country_of_origin = models.CharField(max_length=30)
    birth_year = models.CharField(max_length=5, blank=True, null=True)
    death_year = models.CharField(max_length=5, blank=True, null=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        if(self.first_name is not None):
            return self.last_name + ", " + self.first_name
        return self.last_name

    # override.  Tells django how to find the url for a specific book, after saving it
    def get_absolute_url(self):
        return reverse('author-list')

    class Meta:
        ordering = ['last_name', 'first_name']


class PageFix(models.Model):
    f = models.CharField(max_length=4, default='')


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name='books')
    year_written = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    subcategory = models.CharField(max_length=30, blank=True, null=True)
    standard_pages = models.IntegerField(blank=True, null=True)
    year_read = models.IntegerField(blank=True, null=True)
    enjoyment = models.IntegerField(blank=True, null=True)
   

    def __str__(self):
        return self.title + "  (" + str(self.year_read)+")"

    # override.  Tells django how to find the url for a specific book(?), after saving it
    def get_absolute_url(self):
        return reverse('book-list')

    class Meta:
        ordering = ['year_read','title']
