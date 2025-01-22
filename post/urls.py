from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path(route="", view=views.PostListAPIView.as_view(), name="post_list"),
    path(route="<int:pk>/", view=views.PostDetailAPIView.as_view(), name="post_detail"),
    path(
        route="<int:post_pk>/comments/",
        view=views.CommentListAPIView.as_view(),
        name="comment_list",
    ),
    path(
        route="comments/<int:comment_pk>/",
        view=views.CommentDetailAPIView.as_view(),
        name="comment_detail",
    ),
]
