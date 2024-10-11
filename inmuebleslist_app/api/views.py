from django.shortcuts import get_object_or_404
from inmuebleslist_app.models import Edificacion, Empresa
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
#from rest_framework.decorators import api_view


class EdificacionListAV(APIView):
    
    def get(self, request):
        edificacion = Edificacion.objects.all()
        seri = EdificacionSerializer(edificacion, many=True)
        return Response(seri.data)

    def post(self, request):
        seri = EdificacionSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        else:
            return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)

class EdificacionDetalleAV(APIView):

    def get(self, request, id):
        try:
            edificacion = Edificacion.objects.get(pk = id)
        except Edificacion.DoesNotExist:
            return Response({"Error":"Edificacion no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        data = EdificacionSerializer(edificacion)
        return Response(data.data)


    def put(self, request, id):
        try:
            edificacion = Edificacion.objects.get(pk = id)
        except Edificacion.DoesNotExist:
            return Response({"Error":"Edificacion no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EdificacionSerializer(edificacion, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk = id)
        except Edificacion.DoesNotExist:
            return Response({"Error":"Edificacion no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmpresaAV(APIView):
    def get(self, request):
        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer(empresa, many=True, context={'request':request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetalleAV(APIView):

    def get(self,request, id):
        try:
            empresa = Empresa.objects.get(pk = id)
        except Empresa.DoesNotExist:
            return Response({"Error":"Empresa no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, context={"request":request})
        return Response(serializer.data)
    
    def put(self, request, id):
        try:
            empresa = Empresa.objects.get(pk = id)
        except Empresa.DoesNotExist:
            return Response({"Error":"Empresa no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            empresa = Empresa.objects.get(pk = id)
        except Empresa.DoesNotExist:
            return Response({"Error":"Empresa no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# #SE PUEDEN DEFINIR QUE SEAN DE DOS TIPO Y DEPENDIENDO DE LO QUE ENTRE
# @api_view(['GET', 'POST']) #ES LO MISMO @api_view() 
# def listar_inmuebles(request):

#     if request.method == 'GET':
      
#         inmuebles = Inmueble.objects.all()
#         serializer = InmuebleSerializer(inmuebles, many = True)
#         return Response(serializer.data)


#     elif request.method == 'POST':
#         de_serializer = InmuebleSerializer(data = request.data)

#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
# #comentario
#         else:
#             return Response(de_serializer.errors)

# @api_view(['GET', 'PUT','DELETE'])
# def inmueble_detalle(request, x):

#     if request.method == 'GET':
#         try:
#             inmueble = Inmueble.objects.get(pk = x)
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Inmueble.DoesNotExist:
#             return Response({'Error':'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
    
#     elif request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk = x)

#         de_serializer = InmuebleSerializer(inmueble ,data = request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         try:
#             inmueble = Inmueble.objects.get(pk = x)
#             inmueble.delete()
#         except Inmueble.DoesNotExist:
#             return Response({
#                 "Error":"No existe"
#             }, status=status.HTTP_404_NOT_FOUND
#             )

#         return Response(status=status.HTTP_204_NO_CONTENT)