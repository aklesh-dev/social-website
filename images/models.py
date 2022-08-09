from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
# ---Image model to store images retrieved from different sites.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='image_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to = "images/%Y/%m/%d/")
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    # --- many to many relationships
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='image_liked', blank=True)

    def __str__(self):
        return self.title
    
    # ---slugify function, to automatically generate the image slug
    # ---and save the object. users don't have to manually enter a slug for each image. 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
