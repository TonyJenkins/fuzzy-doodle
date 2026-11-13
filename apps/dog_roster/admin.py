from django.contrib import admin

from apps.dog_roster.models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "breed", "age")
    list_filter = ("breed", "age")
    search_fields = ("name", "breed")
