from django.db import models
from django.conf import settings


# Create your models here.


class UserProfile(models.Model):
    # when user is removed the profile object is also removed

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "Profiles"
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="profile/", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} | {self.last_name}"
