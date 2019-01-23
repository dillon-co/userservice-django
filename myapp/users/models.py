from django.db import models
from django.contrib.auth.models import User
from feed.models import Demographics



class Profile(models.Model):
    GENDER_CHOICES=(
                    ('Male', 'Male'),
                    ('Female', 'Female'),
                    ('Other', 'Other')
                )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    image = models.ImageField(default='default.jpg', upload_to=f'{user}/profile_pics')

# Create your models here.
