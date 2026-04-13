from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}"



class Notes(models.Model):
    class Meta:
        verbose_name = "note"
        verbose_name_plural = "Notes"
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    note = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_public = models.BooleanField(default=False)
    image_attachments = models.ImageField(upload_to="note_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        f"{self.title} | {self.visibility}"


