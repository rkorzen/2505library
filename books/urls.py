from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("", views.list, name="list"),
    path("<int:book_id>/", views.details, name="details")
]