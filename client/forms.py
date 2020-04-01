from .models import Client
from django import forms


class Clientform(forms.ModelForm):
    class Meta:
        model=Client
        fields=[
            'Name',
            'Address',
            'Tel',
            'Gst_no'
        ]