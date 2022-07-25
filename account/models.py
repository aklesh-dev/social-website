from pyexpat import model
from django.db import models
from django.conf import settings

# --User Profile model
# --one to one field allows to associate profiles with users.
# --CASECADE for the on_delete parameter so that its profile also gets deleted
# --when a user is deleted.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_if_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to = 'users/%Y/%m/%d/', blank = True)

    def __str__(self):
        return f'Profile for user {self.user.username}'