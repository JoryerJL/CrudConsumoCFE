from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import State, PostalCode, Municipality, Colony, Client
from .forms import ClientForm

class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_create.html'
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['client_form'] = self.form_class(
                self.request.POST)
        else:
            context['client_form'] = self.form_class()

        return context

    def form_valid(self, form):
        phone_number = form.cleaned_data['phone_number']
        if Client.objects.filter(phone_number=phone_number).exists():
            messages.error("Ya existe un cliente con este número de teléfono")
            return super().form_invalid(form)

        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
