"""
URL configuration for actions with User
"""
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from django.urls import path

from .views import UserViewSet


router = DefaultRouter()
router.register(r"", UserViewSet, "user")


urlpatterns = [
    path(r"token-auth/", obtain_jwt_token),
    path(r"token-refresh/", refresh_jwt_token),
]

urlpatterns += router.urls
