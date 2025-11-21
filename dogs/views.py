from django.shortcuts import render, get_object_or_404
from .models import Dog


def index(request):
    return render(request, "base.html")


def dogs_list(request):
    dogs = Dog.objects.all()
    context = {"dogs": dogs}
    return render(request, "dogs/dogs_list.html", context)


def dogs_details(request, pk):
    # dog = Dog.objects.get(pk=pk)
    dog = get_object_or_404(Dog, pk=pk)
    context = {"dog": dog}
    return render(request, "dogs/dogs_detail.html", context)
