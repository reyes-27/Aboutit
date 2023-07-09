from django import forms
from .models import Post, Comment, Image


class ImageForm(forms.ModelForm):
	image = forms.ImageField(
		label = "image",
		widget=forms.ClearableFileInput(attrs={"multiple":True}),
	)
	class Meta:
		model = Image
		fields = "__all__"

class PostForm(forms.ModelForm):

	class Meta:
		model=Post
		fields=["header", "description", "category"]


class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=("text",)