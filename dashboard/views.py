from django.http import HttpResponse

from tutores.models import Tutor
from pets.models import Pet
from vacinas.models import Vacina
from agenda.models import Agendamento
from atendimentos.models import Atendimento


def dashboard(request):

proximos = Agendamento.objects.all().order_by('data')[:5]

    html = f"""
<html>

<head>
    <title>Vet Domiciliar</title>
</head>

<body style="
font-family:Arial;
background:#f4f6f8;
padding:30px;
">

<div style="
background:#1e293b;
color:white;
padding:20px;
border-radius:15px;
margin-bottom:20px;
box-shadow:0 4px 12px rgba(0,0,0,0.15);
">
    <h1 style="margin:0;">
        🐶 Vet Domiciliar
    </h1>
</div>

<div style="
display:flex;
gap:20px;
flex-wrap:wrap;
">

   <div style="
background:#2563eb;
color:white;
padding:20px;
border-radius:15px;
width:220px;
box-shadow:0 4px 12px rgba(0,0,0,0.15);">
<h3>👤 Tutores</h3>
<h1>{Tutor.objects.count()}</h1>
</div>

    <div style="
background:#16a34a;
color:white;
padding:20px;
border-radius:15px;
width:220px;
box-shadow:0 4px 12px rgba(0,0,0,0.15);">
<h3>🐶 Pets</h3>
<h1>{Pet.objects.count()}</h1>
</div>

    <div style="
background:#dc2626;
color:white;
padding:20px;
border-radius:15px;
width:220px;
box-shadow:0 4px 12px rgba(0,0,0,0.15);">
<h3>💉 Vacinas</h3>
<h1>{Vacina.objects.count()}</h1>
</div>

   <div style="
background:#9333ea;
color:white;
padding:20px;
border-radius:15px;
width:220px;
box-shadow:0 4px 12px rgba(0,0,0,0.15);">
<h3>📅 Agenda</h3>
<h1>{Agendamento.objects.count()}</h1>
</div>

<div style="
background:#f59e0b;
color:white;
padding:20px;
border-radius:15px;
width:220px;
box-shadow:0 4px 12px rgba(0,0,0,0.15);">
<h3>🩺 Atendimentos</h3>
<h1>{Atendimento.objects.count()}</h1>
</div>

</div>

</body>

</html>
"""

    return HttpResponse(html)