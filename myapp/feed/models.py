from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Demographics(models.Model):
    male_count = models.IntegerField(default=0)
    female_count = models.IntegerField(default=0)
    other_count = models.IntegerField(default=0)
