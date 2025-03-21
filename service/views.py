from distutils.command.clean import clean

from django.contrib import messages
from django.shortcuts import render

from .forms import ServiceForm
from .models import Service
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView


# Create your views here.
class ServiceList(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'

class ServiceCreate(CreateView):
    model = Service
    template_name = 'service_create.html'
    form_class = ServiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['service_form'] = self.form_class(
                self.request.POST)
        else:
            context['service_form'] = self.form_class()

        return context


    def form_valid(self, form):
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            if self.request.POST:
                context['service_form'] = self.form_class(
                    self.request.POST)
            else:
                context['service_form'] = self.form_class()

            return context

        service_number = form.cleaned_data['service_number']
        if Service.objects.filter(service_number=service_number).exists():
            messages.error(self.request, "Ya existe un servicio con este numero")
            return redirect('service_create')
        form.save()
        messages.success(self.request, "Servicio creado exitosamente")
        return redirect('service_list')

    def form_invalid(self, form):
        messages.error(self.request, "Error al crear el servicio")
        return redirect('service_create')