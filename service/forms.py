from django import forms
from .models import Service, Rate, Receipt


class ServiceForm(forms.ModelForm):
    service_number = forms.CharField(label='Número de servicio', help_text='Ingresa tu número de servicio',required=True)
    meter_number = forms.CharField(label='Número de medidor', help_text='Ingresa tu número de medidor',required=True)
    rmu = forms.CharField(label='RMU', help_text='Ingresa tu RMU',required=True)
    threads = forms.IntegerField(label='Hilos', help_text='Ingresa el número de hilos',required=True, min_value=1)
    account = forms.CharField(label='Cuenta', help_text='Ingresa tu cuenta',required=True)

    class Meta:
        model = Service
        fields = ['service_number', 'client', 'meter_number', 'rmu', 'rate', 'threads', 'account']

class RateForm(forms.ModelForm):
    rate = forms.DecimalField(label='Rate', help_text='Ingresa tu tarifa',required=True)

    class Meta:
        model = Rate
        fields = ['rate']

class ReceiptForm(forms.ModelForm):
    amount = forms.DecimalField(label='Amount', help_text='Ingresa tu amount',required=True)
    previous_kWh_consumption = forms.DecimalField(label='Consumo de kW anterior', help_text='Ingresa tu consumo de kW anterior',required=True)
    current_kWh_consumption = forms.DecimalField(label='Consumo de kWh actual', help_text='Ingresa tu consumo de kWh actual',required=True)
    start_period = forms.DateField(label='Fecha de inicio del periodo facturado', help_text='Ingresa tu fecha de inicio del periodo facturado',required=True)
    end_period = forms.DateField(label='Fecha de fin del periodo facturado', help_text='Ingresa tu fecha de fin del periodo facturado',required=True)
    total_kWh_consumption = forms.DecimalField(label='Consumo total de kWh', help_text='Ingresa tu consumo total de kWh',required=True)
    payment_deadline = forms.DateField(label='Límite de pago', help_text='Ingresa tu límite de pago',required=True)
    cut_off_date = forms.DateField(label='Fecha de corte', help_text='Ingresa tu fecha de corte',required=True)

    class Meta:
        model = Receipt
        fields = ['service','amount', 'previous_kWh_consumption', 'current_kWh_consumption', 'start_period', 'end_period', 'total_kWh_consumption', 'payment_deadline', 'cut_off_date']