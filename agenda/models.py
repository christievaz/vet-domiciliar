from django.db import models
from pets.models import Pet


class Agendamento(models.Model):

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agenda"

    STATUS_CHOICES = [
        ('Agendado', 'Agendado'),
        ('Confirmado', 'Confirmado'),
        ('Realizado', 'Realizado'),
        ('Cancelado', 'Cancelado'),
    ]

    SERVICO_CHOICES = [
        ('Consulta Clínica', 'Consulta Clínica'),
        ('Vacinação', 'Vacinação'),
        ('Retorno', 'Retorno'),
        ('Procedimento', 'Procedimento'),
        ('Coleta de Exames', 'Coleta de Exames'),
    ]

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    servico = models.CharField(
        max_length=50,
        choices=SERVICO_CHOICES
    )

    data = models.DateField()

    horario = models.TimeField()

    duracao_minutos = models.IntegerField(
        default=60
    )

    endereco = models.CharField(
        max_length=255
    )

    observacoes = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Agendado'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.pet.nome} - {self.data}"