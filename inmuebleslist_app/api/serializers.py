from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

class InmuebleSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only = True)
    direccion = serializers.CharField()
    pais = serializers.CharField()
    descipcion = serializers.CharField()
    active = serializers.BooleanField()
    imagen = serializers.CharField()

    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.descipcion = validated_data.get('descipcion', instance.descipcion)
        instance.active = validated_data.get('active' , instance.active)
        instance.save()
        return instance