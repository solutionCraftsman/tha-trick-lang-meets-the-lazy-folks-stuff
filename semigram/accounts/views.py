from django.shortcuts import render

# Create your views here.
from accounts.forms import OwnerInformation


def create_user(request):
    if request.method == 'POST':
        form = OwnerInformation(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    else:
        form = OwnerInformation()
        context = {
            "form": form
        }
        return render(request, "user_creation.html", context)
