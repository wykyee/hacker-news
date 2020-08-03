from django.urls import path, include

urlpatterns = [
    path("user/", include("api.users.urls")),
    path("post/", include("api.posts.urls")),
    path("comments/", include("api.comments.urls")),
]
