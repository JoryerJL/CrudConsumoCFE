from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import State, PostalCode, Municipality, Colony, Client
from .forms import ClientForm, StateForm, PostalCodeForm, ColonyForm, MunicipalityForm

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
            context['client_form'] = self.form_class(self.request.POST or None)
            context['municipality_form'] = MunicipalityForm(self.request.POST or None)
            context['state_form'] = StateForm(self.request.POST or None)
            context['postal_code_form'] = PostalCodeForm(self.request.POST or None)
            context['colony_form'] = ColonyForm(self.request.POST or None)
        else:
            context['client_form'] = self.form_class()
            context['municipality_form'] = MunicipalityForm()
            context['state_form'] = StateForm()
            context['postal_code_form'] = PostalCodeForm()
            context['colony_form'] = ColonyForm()
        return context

    def form_valid(self, form):
        phone_number = form.cleaned_data['phone_number']
        if Client.objects.filter(phone_number=phone_number).exists():
            messages.error("Ya existe un cliente con este número de teléfono")
            return super().form_invalid(form)

        form.save()
        return redirect('client_list')

    def form_invalid(self, form):
        return super().form_invalid(form)

def add_state(request):
    if request.method == 'POST':
        state_form = StateForm(request.POST)
        if state_form.is_valid():
            state_form.save()
            messages.success(request, "Estado agregado exitosamente")
        else:
            messages.error(request, "Error al agregar el estado")
    return redirect('client_create')

def add_postal_code(request):
    if request.method == 'POST':
        postal_code_form = PostalCodeForm(request.POST)
        if postal_code_form.is_valid():
            postal_code = postal_code_form.cleaned_data.get('postal_code')
            if PostalCode.objects.filter(postal_code=postal_code).exists():
                messages.error(request, "Ya existe un código postal con este número")
            else:
                postal_code_form.save()
                messages.success(request, "Código Postal agregado exitosamente")
        else:
            messages.error(request, "Error al agregar el Código Postal")
    return redirect('client_create')

def add_colony(request):
    if request.method == 'POST':
        colony_form = ColonyForm(request.POST)
        if colony_form.is_valid():
            colony_form.save()
            messages.success(request, "Colonia agregada exitosamente")
        else:
            messages.error(request, "Error al agregar la colonia")
    return redirect('client_create')

def add_municipality(request):
    if request.method == 'POST':
        municipality_form = MunicipalityForm(request.POST)
        if municipality_form.is_valid():
            municipality_form.save()
            messages.success(request, "Municipio agregado exitosamente")
        else:
            messages.error(request, "Error al agregar el municipio")
    return redirect('client_create')
