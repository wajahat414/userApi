from django.urls import path
from .views import UserListCreateView, UserDetailView
from .views import download_zip


urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("download_zip/", download_zip, name="download_zip"),
]
