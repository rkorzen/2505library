from django.urls import path

from users.views import dashboard, example_view

urlpatterns = [
    path("", dashboard, name='dashboard'),
    path("examples/formform", example_view, name='example_form')
]

