from django import forms
from user.models import Merchant


class MerchantInfo(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'
