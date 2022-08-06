from django.urls import path

from . import views

app_name = "authors"
urlpatterns = [
    path("", views.list, name="list"),
    path("<int:author_id>/", views.details, name="details")
]