from django.contrib.auth.models import AbstractUser
from django.db import models
from oxcimarron.utils import validate_file_size
from django.core.validators import MaxValueValidator


class CustomUser(AbstractUser):

    # add additional fields in here
    zip_code = models.IntegerField(blank=True, null=True, validators=[
                                   MaxValueValidator(99999)])
    photo = models.ImageField(
        upload_to='images/', blank=True, null=True, validators=[validate_file_size])

    def __str__(self):
        return self.username
