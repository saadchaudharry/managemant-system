from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Client
from .forms import Clientform


# Create your views here.

class ClientView(CreateView):
    model = Client
    form_class = Clientform
    template_name = 'client.html'
    success_url = "/1/"

class Clientlist(ListView):
    queryset = Client.objects.all()
    template_name = 'clientlist.html'