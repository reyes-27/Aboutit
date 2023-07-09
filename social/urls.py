from django.urls import path
from .views import (
	FeedListView,
	PostCreateView,
	RePostView,
	PostDetailView,
	PostUpdateView,
	LikeView,
	DislikeView,
	CommentCreateView,
	AnswerView,
	)


urlpatterns=[
	path('', FeedListView.as_view(), name="feed"),
	path('repost/<uuid:id>/', RePostView.as_view(), name="create_repost"),
	path('post/new/', PostCreateView.as_view(), name="create_post"),
	path('post/<uuid:pk>/', PostDetailView.as_view(), name="post_detail"),
	path('post/edit/<uuid:pk>/', PostUpdateView.as_view(), name="update_post"),
	path("like/<uuid:pk>/", LikeView.as_view(), name="like"),
	path("dislike/<uuid:pk>/", DislikeView.as_view(), name="dislike"),
	path("comment/<uuid:pk>/", CommentCreateView.as_view(), name="create_comment"),
	path("answer/<uuid:pk>/", AnswerView.as_view(), name="create_answer"),
]