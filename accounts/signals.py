from .models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from social.models import UserProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		new_profile=UserProfile.objects.create(user=instance)
		new_profile.username=instance.username

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
	instance.user_profile.save()