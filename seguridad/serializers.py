from rest_framework import serializers
from seguridad.models import User
from seguridad.models import Verificacion
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from decouple import config

# Serializers define the API representation.
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.correo = user.username
        arrCadena = user.username.split("@")
        user.nombre_corto = arrCadena[0]
        user.is_active = False
        user.imagen = f"celio/usuario/imagen_defecto.jpg"
        user.set_password(validated_data['password'])    
        user.save()
        return user

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'correo': instance.correo,
            'dominio': instance.dominio,
            'nombre_corto': instance.nombre_corto,
            'nombre': instance.nombre,
            'apellido': instance.apellido,
            'telefono': instance.telefono,
            'idioma': instance.idioma,
            'vr_saldo': instance.vr_saldo,
            'imagen': f"https://{config('DO_BUCKET')}.{config('DO_REGION')}.digitaloceanspaces.com/{instance.imagen}",
            'fecha_limite_pago': instance.fecha_limite_pago
        }

class UserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['nombre_corto', 'nombre', 'apellido', 'telefono', 'idioma']

class VerificacionSerializador(serializers.ModelSerializer):
    class Meta:
        model = Verificacion
        fields = ['id', 'token', 'estado_usado', 'vence', 'accion', 'usuario_id', 'contenedor_id', 'usuario_invitado_username']              
       