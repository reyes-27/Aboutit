from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

User=get_user_model()


class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
	username=models.CharField(max_length=20)
	bio=models.CharField(max_length=255, blank=True, null=True)
	profile_pic=models.ImageField(upload_to="profile_pic/", default="profile_pic/default.jpg")

class Category(models.Model):
	# category_choices=(
	# 	("SPO", "Sports"),
	# 	("TEC", "Tech"),
	# 	("ART", "Art"),
	# 	("FAS", "Fashion"),
	# )
	category_name=models.CharField(max_length=40, null=True,)
	def __str__(self):
		return self.category_name


class Post(models.Model):
	parent=models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="post_parent")
	repost=models.ManyToManyField("self", blank=True, symmetrical=False)
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
	header=models.CharField(max_length=255)
	description=RichTextField(blank=True, null=True)
	pub_date=models.DateTimeField(auto_now_add=True)
	category=models.ManyToManyField(Category, related_name="posts")
	likes=models.PositiveIntegerField(default=0)
	dislikes=models.PositiveIntegerField(default=0)
	user_dislikes=models.ManyToManyField(User, blank=True, related_name="user_dislikes")
	user_likes=models.ManyToManyField(User, blank=True, related_name="user_likes")
	
	def __str__(self):
		return self.header

	def get_absolute_url(self):
		return reverse("post_detail", args=[str(self.id)])

class Like(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_likes")
	post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts_likes")
	already_liked=models.BooleanField(default=False)
	def __str__(self):
		return f"{self.user} liked {self.post}"

class Dislike(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_dislikes")
	post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts_dislikes")
	already_disliked=models.BooleanField(default=False)
	def __str__(self):
		return f"{self.user} didn\'t like {self.post}"

class Comment(models.Model):
	comment_parent=models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
	comment_child=models.ManyToManyField("self", blank=True, symmetrical=False, related_name="comment_childs")
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	text=models.TextField()
	pub_date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text

	def get_absolute_url(self):
		return reverse("comment_detail", kwargs={"pk": self.pk})
	

class Image(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="image")
	image=models.ImageField(upload_to="post_images/", blank=True, null=True)
