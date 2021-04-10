from django.shortcuts import render
from gallery.models import MenDem


# Create your views here.
def gallery_index(request):
    men_dem = MenDem.objects.all()
    context = {
        'men_dem': men_dem
    }
    return render(request, 'gallery_index.html', context)


def man_details(request, pk):
    man = MenDem.objects.get(pk=pk)
    context = {
        'man': man
    }
    return render(request, 'man_details.html', context)


