from django.db import models
from pets.models import Pet


class Vacina(models.Model):

    class Meta:
        verbose_name = "Vacina"
        verbose_name_plural = "Vacinas"

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    protocolo = models.CharField(max_length=100)

    fabricante = models.CharField(max_length=100)

    data_aplicacao = models.DateField()

    lote = models.CharField(max_length=50)

    validade = models.DateField()

    proxima_dose = models.DateField(
        null=True,
        blank=True
    )

    veterinaria_responsavel = models.CharField(
        max_length=100,
        blank=True
    )

    observacoes = models.TextField(
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.pet.nome} - {self.protocolo}"