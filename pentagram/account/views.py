from django.shortcuts import render
from account.form import OwnerInformation


# Create your views here.
def home(request):
    return render(request, 'account/home.html')


def create_user(request):
    if request.method == 'POST':
        form = OwnerInformation(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = OwnerInformation()
        context = {
            'form': form
        }
        return render(request, 'user/user_creation.html')