from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "user"
urlpatterns = [
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(route="", view=views.UserListAPIView.as_view(), name="user_list"),
    path(route="<int:pk>/", view=views.UserDetailAPIView.as_view(), name="user_detail"),
]
