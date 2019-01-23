from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from feed.models import Demographics


def current_demographics():
    if Demographics.objects.all().count() > 0:
        c_d = Demographics.objects.all().last()
        return c_d.male_count, c_d.female_count, c_d.other_count
    else:
        0, 0, 0

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    male_count, female_count, other_count = current_demographics()
    if instance.profile.gender == 'Male':
        male_count += 1
    elif instance.profile.gender == 'Female':
        female_count += 1
    elif instance.profile.gender == 'Other':
        other_count += 1

    Demographics.objects.create(male_count=male_count, female_count=female_count, other_count=other_count)
