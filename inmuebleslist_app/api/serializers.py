from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa, Comentario

class ComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = "__all__"

class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many = True, read_only=True)
    #campos antes del meta
    #campos que aparecen despues
    class Meta:
        model = Edificacion
        #fields = "__all__"
        # fields = [
        #     'id',
        #     'pais',
        #     'active',
        # ]

        exclude = ['id', 'active']

    def get_longitud_direccion(self, object):
        cantidad = len(object.direccion)
        return cantidad

    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError('La dir y el pais deben ser diferentes')
        else:
            return data 
        
    def validate_imagen(self, data):
         if len(data) < 2:
             raise serializers.ValidationError('Url muy corta')
         else:
             return data
         
class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    edificacion_list = EdificacionSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='empresa-detalle', lookup_field='id')

#   edificacion_list = serializers.StringRelatedField(many=True, read_only=True) lo que devuelve el __str__
#   edificacion_list = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #para devilver la llave(id)
    # edificacion_list = serializers.HyperlinkedRelatedField(
        # many=True, 
        # read_only=True,
        # view_name='edificacion-detalle',
        # lookup_field='id'
    # )

    class Meta:
        model = Empresa
        fields = "__all__"




# def column_longitud(value):

#     if len(value) < 2 :
#         raise serializers.ValidationError("La direccion es demasiado corta")

# class InmuebleSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only = True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField()
#     descipcion = serializers.CharField()
#     active = serializers.BooleanField()
#     imagen = serializers.CharField()

#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.descipcion = validated_data.get('descipcion', instance.descipcion)
#         instance.active = validated_data.get('active' , instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError('La dir y el pais deben ser diferentes')
#         else:
#             return data 
        
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError('Url muy corta')
#         else:
#             return data
    
