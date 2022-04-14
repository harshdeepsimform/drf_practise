from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, CustomUser
from station.utils import get_location


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    print("############## create profile signal called")
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save, sender=Profile)
# def save_profile(sender, instance, created, **kwargs):
#     print("############ update profile signal called.", instance.address)
#     # import pdb; pdb.set_trace()
#     if instance.address:
#         lat, lon = get_location(instance.address) 

#         # profile = Profile.objects.get(user=instance)
#         instance.latitude = lat
#         instance.longitude = lon
#         instance.save()
