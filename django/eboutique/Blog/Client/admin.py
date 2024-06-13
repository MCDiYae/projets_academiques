from django.contrib import admin

from Client.models import Client, ClientAdmin

# Register your models here.
admin.site.register(Client, ClientAdmin)
