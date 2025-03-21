from django.shortcuts import render
from .models import Service
from django.views.generic import ListView, CreateView


# Create your views here.
class ServiceList(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'

class ServiceCreate(CreateView):
    model = Service
    template_name = 'service_create.html'
    form_class = Service