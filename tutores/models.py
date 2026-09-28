from django.db import models


class Tutor(models.Model):

    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

    nome = models.CharField(max_length=200)
    sexo = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)

    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(
        max_length=100,
        blank=True
    )

    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    como_conheceu = models.CharField(max_length=100)

    def __str__(self):
        return self.nome