from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from oxcimarron.utils import Utils
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(
        upload_to='images/', blank=True, null=True)  # was ImageField

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])


class Comment(models.Model):

    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments',)
    print("ARTICLE: ", article)
    comment = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    author = models.CharField(max_length=16, default='Test1', blank=True)
    approved_comment = models.BooleanField(
        default=False, null=True, blank=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
