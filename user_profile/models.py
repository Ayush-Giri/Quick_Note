from django.db import models
from django.conf import settings


# Create your models here.


class UserProfile(models.Model):
    # when user is removed the profile object is also removed
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="profile/", null=True, blank=True)
