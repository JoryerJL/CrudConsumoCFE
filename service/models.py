from django.db import models
from client.models import Client
from common.models import CommonBaseModel

class Rate(CommonBaseModel):
    rate = models.DecimalField("Tarifa",max_digits=10, decimal_places=2)

class Service(CommonBaseModel):
    service_number = models.PositiveIntegerField("Número de servicio")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    meter_number = models.CharField("Número de medidor",max_length=11)
    rmu = models.CharField("RMU",max_length=100)
    rate = models.ForeignKey('Rate', on_delete=models.CASCADE)
    threads = models.PositiveIntegerField("Hilos")
    account = models.CharField("Cuenta",max_length=100)


class Receipt(CommonBaseModel):
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    previous_kWh_consumption = models.DecimalField("Consumo de kW anterior", max_digits=10, decimal_places=2)
    current_kWh_consumption = models.DecimalField("Consumo de kWh actual", max_digits=10, decimal_places=2)
    start_period = models.DateField("Fecha de inicio del periodo facturado")
    end_period = models.DateField("Fecha de fin del periodo facturado")
    total_kWh_consumption = models.DecimalField("Consumo total de kWh", max_digits=10, decimal_places=2)
    payment_deadline = models.DateField("Límite de pago")
    cut_off_date = models.DateField("Fecha de corte")

