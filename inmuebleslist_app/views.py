from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from inmuebleslist_app.models import Inmueble

# Create your views here.


def listar_inmuebles(request):

    inmuebles = Inmueble.objects.all()
    data = {
        'inmuebles':list(inmuebles.values())
    }

    return JsonResponse(data)


def inmueble_for_id(request, x):
    
    inmueble = get_object_or_404(Inmueble, id = x)
    data = {
        'direccion' : inmueble.direccion,
        'pais' : inmueble.descipcion,
        'imagem' : inmueble.imagen,
        'activo' : inmueble.active,
        'desc' : inmueble.descipcion
    }

    return JsonResponse(data)