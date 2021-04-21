from django.shortcuts import render
from user.forms import MerchantInfo


# Create your views here.
def create_merchant(request):

    if request.method == 'POST':
        form = MerchantInfo(request.POST, request.FILES)

        if form.is_valid():
            message = "Merchant not created"
            if form.save():
                message = "Merchant created"
            return render(request, 'info.html', context={'message': message})

    return render(request, 'user/create/create_merchant.html', context={'form': MerchantInfo()})
