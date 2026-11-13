from django.urls import path
from . import views

app_name = "apps.dog_roster"

urlpatterns = [
    path("", views.index, name="index"),
    path("dog/<int:pk>", views.dog_detail, name="dog_detail"),
]
