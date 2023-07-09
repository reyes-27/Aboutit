from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import redirect
from .models import Post, Comment
from django.urls import reverse

@receiver(post_save, sender=Post)
def link_post_its_child(sender, instance, created, **kwargs):
	if created:
		print("created")
		if instance.parent != None:
			print("it\'s a repost")

			parent=instance.parent
			parent=Post.objects.get(id=parent.id)
			parent.repost.add(instance)

			redirect(reverse("feed"))

@receiver(post_save, sender=Comment)
def link_comment_to_its_child(sender, instance, created, **kwargs):
	if created:
		if instance.comment_parent != None:
			parent=instance.comment_parent
			comment_parent=Comment.objects.get(id=parent.id)
			comment_parent.comment_child.add(instance)

