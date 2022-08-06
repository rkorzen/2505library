from django.urls import path

from posts import views

app_name = "posts"
urlpatterns = [
    path("", views.listview, name="list"),
    path("<int:post_id>", views.details, name="details")
]