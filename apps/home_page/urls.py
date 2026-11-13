from django.urls import include, path

from . import views

app_name = "home_page"

urlpatterns = [
    path("", views.index, name="index"),
]
