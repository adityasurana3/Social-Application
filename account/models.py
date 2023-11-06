from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null= True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return f'Profile of {self.user.username}'

# Signal to create a profile whenever a user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile,sender=settings.AUTH_USER_MODEL)