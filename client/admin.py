from django.contrib import admin
from .models import Client,ClientBalance
# Register your models here.

admin.site.register(Client)
admin.site.register(ClientBalance)