from django import forms
from apps.service.models import Service
from apps.user.models import Subscription


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['service_name', 'payment_terms', 'service_price', 'service_package', 'service_image','active' ]



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model=Subscription
        fields=["address"]