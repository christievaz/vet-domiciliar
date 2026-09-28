from django.db import models
from tutores.models import Tutor


class Pet(models.Model):

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE
    )

    nome = models.CharField(max_length=100)

    especie = models.CharField(max_length=50)

    raca = models.CharField(max_length=100)

    sexo = models.CharField(max_length=20)

    data_nascimento = models.DateField(
        null=True,
        blank=True
    )

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    microchip = models.CharField(
        max_length=50,
        blank=True
    )

    pelagem = models.CharField(
        max_length=100,
        blank=True
    )

    temperamento = models.CharField(
        max_length=100,
        blank=True
    )

    castrado = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.nome