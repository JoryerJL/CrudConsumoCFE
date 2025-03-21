from django.db import models
from common.models import CommonBaseModel

class State(CommonBaseModel):
    name = models.CharField("Nombre", max_length=100)
    def __str__(self):
        return self.name

class Municipality(CommonBaseModel):
    name = models.CharField("Nombre", max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PostalCode(CommonBaseModel):
    postal_code = models.PositiveBigIntegerField("Código postal")
    municipality = models.ForeignKey('Municipality', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postal_code)

class Colony(CommonBaseModel):
    name = models.CharField("Nombre", max_length=100)
    postal_code = models.ForeignKey(PostalCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
class Client(CommonBaseModel):
    name = models.CharField("Nombre", max_length=100)
    paternal_surname = models.CharField("Apellido Paterno", max_length=100)
    maternal_surname = models.CharField("Apellido Materno", max_length=100)
    phone_number = models.CharField("Número de teléfono", max_length=10)
    street = models.CharField("Calle", max_length=100)
    interior_number = models.CharField("Número interior", null=True, blank=True)
    external_number = models.CharField("Exteranl interior", null=True, blank=True)
    colony = models.ForeignKey(Colony, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.paternal_surname} {self.maternal_surname}"

    def get_full_name(self):
        return f"{self.name} {self.paternal_surname} {self.maternal_surname}"

    def get_full_address(self):
        return (f"{self.street} {self.interior_number} {self.external_number} {self.colony} "
                f"{self.colony.postal_code.municipality} "
                f"{self.colony.postal_code.municipality.state} {self.colony.postal_code}")
