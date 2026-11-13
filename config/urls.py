from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dogs/", include("apps.dog_roster.urls", namespace="dog_roster")),
    path("", include("apps.home_page.urls", namespace="home_page")),
]