from django.shortcuts import get_object_or_404
from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer
from rest_framework.response import Response
# Create your views here.

from rest_framework.decorators import api_view


#SE PUEDEN DEFINIR QUE SEAN DE DOS TIPO Y DEPENDIENDO DE LO QUE ENTRE
@api_view(['GET', 'POST']) #ES LO MISMO @api_view() 
def listar_inmuebles(request):

    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many = True)
        return Response(serializer.data)


    elif request.method == 'POST':
        de_serializer = InmuebleSerializer(data = request.data)

        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)

        else:
            return Response(de_serializer.errors)

@api_view(['GET', 'PUT','DELETE'])
def inmueble_detalle(request, x):
    inmueble = get_object_or_404(Inmueble, pk = x)
    if request.method == 'GET':
        
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        
        de_serializer = InmuebleSerializer(inmueble ,data = request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)

    elif request.method == 'DELETE':
        
        inmueble.delete()

        data = {
            'resultado':True
        }

        return Response(data)