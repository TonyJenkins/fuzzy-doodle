from django.shortcuts import render

from apps.dog_roster.models import Dog


def index(request):

    context = {
        "all_dogs": Dog.objects.all(),
    }

    return render(request, "dog_roster/index.html", context)


def dog_detail(request, pk):
    dog = Dog.objects.get(pk=1)
    context = {
        "dog": dog,
    }
    return render(request, "dog_roster/dog_detail.html", context)
