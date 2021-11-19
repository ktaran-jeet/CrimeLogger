from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import os

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    # pip install pillow to use this!
    profile_pic = models.ImageField(upload_to='profile_pics', default='media/profile_pics/69.jpg')

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
    @property
    def filename(self):
        return os.path.basename(self.profile_pic.name)
