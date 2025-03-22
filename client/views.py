from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import State, PostalCode, Municipality, Colony, Client

class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'

