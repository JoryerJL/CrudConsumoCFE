from django.contrib import admin
from service.models import Service, Rate, Receipt

# Register your models here.
admin.site.register(Service)
admin.site.register(Rate)
admin.site.register(Receipt)