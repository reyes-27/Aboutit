from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .models import Post, Like, Dislike, Comment
from .forms import PostForm, CommentForm, ImageForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
# Create your views here.

User=get_user_model()

class FeedListView(ListView):
	model=Post
	context_object_name="posts"
	ordering=["pub_date"]
	template_name="feed.html"

class LikeView(View):

	def post(self, request, pk, *args, **kwargs):
		user=self.request.user
		post=Post.objects.get(pk=pk)
		new_like=Like(user=user, post=post)
		dislike=Dislike(user=user, post=post)
		if user in post.user_likes.all():
			new_like.already_liked=False
			post.likes-=1
			post.user_likes.remove(user)
		else:
			new_like.already_liked=True
			post.likes+=1
			post.user_likes.add(user)
			if user in post.user_dislikes.all():
				dislike.already_disliked=False
				post.dislikes-=1
				post.user_dislikes.remove(user)
		post.save()
		next=request.POST.get("next", "/")
		return HttpResponseRedirect(next)

class DislikeView(View):
	def post(self, request, pk, *args, **kwargs):
		user=request.user
		post=Post.objects.get(pk=pk)
		new_dislike=Dislike(user=user, post=post)
		like=Like(user=user, post=post)
		if user in post.user_dislikes.all():
			new_dislike.already_disliked=False
			post.dislikes-=1
			post.user_dislikes.remove(user)
		else:
			new_dislike.already_disliked=True
			post.dislikes+=1
			post.user_dislikes.add(user)
			if user in post.user_likes.all():
				like.already_liked=False
				post.likes-=1
				post.user_likes.remove(user)


		post.save()
		next=request.POST.get("next", "/")
		return HttpResponseRedirect(next)


class PostCreateView(CreateView):
	model=Post
	template_name="post_new.html"
	fields=[
		"header",
		"description",
		"category",
		]
	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	success_url=reverse_lazy("feed")



class RepostGet(DetailView):
	model=Post
	template_name="repost_new.html"
	def get_object(self, **kwargs):
		object = Post.objects.get(id=self.kwargs['id'])
		#object = get_object_or_404(Post, pk=self.kwargs["id"])
		return object

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context["form"]=PostForm()
		return context

class RepostPost(CreateView):
	model=Post
	template_name="repost_new.html"
	form_class=PostForm

	def get_object(self, **kwargs):
		object = Post.objects.get(id=self.kwargs["id"])
		return object

	def form_valid(self, form, **kwargs):
		#repost=form.save(commit=False)
		parent=Post.objects.get(id=self.kwargs["id"])
		form.instance.author=self.request.user
		form.instance.parent=parent
		return super().form_valid(form)
	
	def post(self, request, *args, **kwargs):
		self.object=self.get_object()
		return super().post(request, *args, **kwargs)

	success_url=reverse_lazy("feed")

class RePostView(View):

	def get(self, request, *args, **kwargs):
		view=RepostGet.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view=RepostPost.as_view()
		return view(request, *args, **kwargs)

class PostUpdateView(UpdateView):
	model=Post
	fields=["header", "description", "image",]
	template_name="update_post.html"
	#def get_context_data(self, **kwargs):
	#	context=super().get_context_data(**kwargs)
	#	context["form"]=PostForm()
	#	return context

class PostDetailView(DetailView):
	model=Post
	template_name="post_detail.html"

class CommentCreateView(CreateView):
	model=Comment
	template_name="comment_create.html"
	form_class=CommentForm
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		post=Post.objects.get(pk=self.kwargs["pk"])
		context.update(
			{'post':post}
		)
		return context

	def form_valid(self, form, **kwargs):
		post=Post.objects.get(pk=self.kwargs["pk"])
		user=self.request.user
		form.instance.post=post
		form.instance.author=user
		return super().form_valid(form)

	success_url=reverse_lazy("feed")

class AnswerGet(DetailView):
	model=Comment
	template_name="comment_create.html"
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context["form"]=CommentForm()
		return context
class AnswerPost(CreateView):
	model=Comment
	form_class=CommentForm
	template_name="comment_create.html"
	def form_valid(self, form, **kwargs):
		comment_parent=Comment.objects.get(pk=self.kwargs["pk"])
		form.instance.post=comment_parent.post
		form.instance.author=self.request.user
		form.instance.comment_parent=comment_parent
		return super().form_valid(form)
	success_url=reverse_lazy("feed")
class AnswerView(View):
	def get(self, request, *args, **kwargs):
		view=AnswerGet.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view=AnswerPost.as_view()
		return view(request, *args, **kwargs)