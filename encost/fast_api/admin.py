from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Client, ClientInfo, Endpoint, EndpointStates

admin.site.unregister(Group)
admin.site.register(ClientInfo)
admin.site.register(Endpoint)
admin.site.register(EndpointStates)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_info')
