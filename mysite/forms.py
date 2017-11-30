from django import forms
from mysite.models import Order
from mysite.models import Pizza


class OrderForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Order
        fields = ('pizza', 'name', 'phone')