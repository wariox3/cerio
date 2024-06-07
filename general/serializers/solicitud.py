from general.models.solicitud import Solicitud
from general.models.ciudad import Ciudad
from transporte.models.carroceria import Carroceria
from seguridad.models import User
from rest_framework import serializers

class SolicitudSerializador(serializers.HyperlinkedModelSerializer):
    carroceria = serializers.PrimaryKeyRelatedField(queryset=Carroceria.objects.all())
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    usuario_asignado = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=None, allow_null=True)
    ciudad_origen = serializers.PrimaryKeyRelatedField(queryset=Ciudad.objects.all())
    ciudad_destino = serializers.PrimaryKeyRelatedField(queryset=Ciudad.objects.all())  
    class Meta:
        model = Solicitud
        fields = ['id', 'fecha', 'descripcion', 'precio', 'peso', 'volumen', 'entregas', 'carroceria', 'usuario', 'usuario_asignado', 'ciudad_origen', 'ciudad_destino']  
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
        }          