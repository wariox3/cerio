from general.models.solicitud import Solicitud
from rest_framework import serializers

class SolicitudSerializador(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id', 'carroceria']  
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
        }          