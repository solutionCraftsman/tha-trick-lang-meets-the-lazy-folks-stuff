from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo


def index(request):
    if request.method == 'POST':
        photo_form = PhotoForm(request.POST)

        if photo_form.is_valid():
            photo_form.save()
        return redirect('photos_index')

    else:
        photo_form = PhotoForm()
        photos = Photo.objects.all()
        context = {
            'photos': photos,
            'photo_form': photo_form
        }
        return render(request, 'photos/index.html', context)
