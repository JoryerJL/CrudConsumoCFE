from .views import ServiceList, ServiceCreate
from django.urls import path, include

urlpatterns = [
    path('', ServiceList.as_view(), name='service_list'),
    path('create/', ServiceCreate.as_view(), name='service_create'),
]
