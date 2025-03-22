from django.contrib import admin

# Register your models here.
from .models import Client, State, Municipality, PostalCode, Colony
admin.site.register(Client)
admin.site.register(State)
admin.site.register(Municipality)
admin.site.register(PostalCode)
admin.site.register(Colony)

