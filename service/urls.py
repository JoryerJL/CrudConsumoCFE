from .views import ServiceList
from django.urls import path, include

urlpatterns = [
    path('', ServiceList.as_view(), name='service_list'),
]
