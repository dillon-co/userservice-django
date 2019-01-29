from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from feed.models import Demographics


def current_demographics():
    if Demographics.objects.all().count() > 0:
        d_id = Demographics.objects.all().last().id
        c_d = Demographics.objects.get(pk=d_id)
        print(f'\n\n\n{c_d}\n\n')
        # return c_d
    else:
        c_d = Demographics.objects.create(male_count=0, female_count=0, other_count=0)
    return c_d

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    d_obj = current_demographics()
    if instance.profile.gender == 'Male':
        male_count = d_obj.male_count + 1
        d_obj.male_count=male_count
    elif instance.profile.gender == 'Female':
        female_count = d_obj.female_count + 1
        d_obj.female_count=female_count
    elif instance.profile.gender == 'Other':
        otehr_count = d_obj.otehr_count + 1
        d_obj.otehr_count=otehr_count

    d_obj.save()
