from django.db import models
from pets.models import Pet


class Atendimento(models.Model):

    class Meta:
        verbose_name = "Atendimento"
        verbose_name_plural = "Atendimentos"

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    data = models.DateField()

    historico_anamnese = models.TextField()

    exame_fisico = models.TextField()

    diagnostico = models.TextField()

    tratamento = models.TextField()

    exames = models.TextField(
        blank=True
    )

    receituario = models.TextField(
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.pet.nome} - {self.data}"