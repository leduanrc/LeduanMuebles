from django.shortcuts import render
from InfoApp.models import Information
from ModelosApp.models import Mueble
from OfertasApp.models import Oferta


# Create your views here.

# Pagina principal
def home(request):
    ofertas = Oferta.objects.all()
    informations = Information.objects.all()
    return render(request, "home.html", {"ofertas":ofertas, "informations":informations})

# MUEBLES
def platanitos(request):
    muebles = Mueble.objects.all()
    return render(request, "platanitos.html", {"muebles":muebles})

def brasilenos(request):
    muebles = Mueble.objects.all()
    return render(request, "brasilenos.html", {"muebles":muebles})

def pelotas(request):
    muebles = Mueble.objects.all()
    return render(request, "pelotas.html", {"muebles":muebles})

def charlottes(request): 
    muebles = Mueble.objects.all()
    return render(request, "charlotte.html", {"muebles":muebles})

def panchos(request):
    muebles = Mueble.objects.all()
    return render(request, "panchos.html", {"muebles":muebles})

def rottweilers(request):
    muebles = Mueble.objects.all()
    return render(request, "rottweilers.html", {"muebles":muebles})

def chesters(request):
    muebles = Mueble.objects.all()
    return render(request, "chesters.html", {"muebles":muebles})

def comadritas(request):
    muebles = Mueble.objects.all()
    return render(request, "comadritas.html", {"muebles":muebles})

def sillones(request):
    muebles = Mueble.objects.all()
    return render(request, "sillones.html", {"muebles":muebles})

# COMEDORES
def comedor4(request):
    muebles = Mueble.objects.all()
    return render(request, "comedor4.html", {"muebles":muebles})

def comedor6(request):
    muebles = Mueble.objects.all()
    return render(request, "comedor6.html", {"muebles":muebles})

def banquetas(request):
    muebles = Mueble.objects.all()
    return render(request, "banquetas.html", {"muebles":muebles})

# CAMAS
def hierro(request):
    muebles = Mueble.objects.all()
    return render(request, "hierro.html", {"muebles":muebles})

def madera(request):
    muebles = Mueble.objects.all()
    return render(request, "madera.html", {"muebles":muebles})

def capitoniada(request):
    muebles = Mueble.objects.all()
    return render(request, "capitoniada.html", {"muebles":muebles})

def comoda(request):
    muebles = Mueble.objects.all()
    return render(request, "comoda.html", {"muebles":muebles})