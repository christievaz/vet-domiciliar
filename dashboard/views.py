from django.shortcuts import render

from tutores.models import Tutor
from pets.models import Pet
from vacinas.models import Vacina
from agenda.models import Agendamento
from atendimentos.models import Atendimento


def dashboard(request):

    context = {
        "tutores": Tutor.objects.count(),
        "pets": Pet.objects.count(),
        "vacinas": Vacina.objects.count(),
        "agenda": Agendamento.objects.count(),
        "atendimentos": Atendimento.objects.count(),
        "proximos": Agendamento.objects.order_by("data")[:5],

        "ultimos_atendimentos": Atendimento.objects.order_by("-id")[:5],
    }

    return render(
        request,
        "dashboard/index.html",
        context
    )