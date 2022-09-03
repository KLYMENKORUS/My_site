import datetime

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    about_myself = models.TextField(max_length=500, default='Bio')

    def __str__(self):
        return f'Profile for user {self.user.username}'

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return '/static/images/default.jpg'



