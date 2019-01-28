from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from feed.models import Demographics


def current_demographics():
    if Demographics.objects.all().count() > 0:
        c_d = Demographics.objects.all().last()
        # return c_d
    else:
        c_d = Demographics.objects.create(male_count:0, female_count:0, other_count:0)
    return c_d

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    demographics = current_demographics()
    if instance.profile.gender == 'Male':
        male_count = demographics.male_count + 1
        demographics.update(male_count: male_count)
    elif instance.profile.gender == 'Female':
        female_count = demographics.female_count + 1
        demographics.update(female_count: female_count)
    elif instance.profile.gender == 'Other':
        otehr_count = demographics.otehr_count + 1
        demographics.update(otehr_count: otehr_count)

    demographics.save()
