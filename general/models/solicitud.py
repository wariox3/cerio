from django.db import models
from general.models.ciudad import Ciudad
from transporte.models.carroceria import Carroceria
from seguridad.models import User

class Solicitud(models.Model):    
    fecha = models.DateField(null=True)
    descripcion = models.CharField(max_length=200, null=True) 
    precio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    peso = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    volumen = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    entregas = models.IntegerField(default=0)
    estado_asignado = models.BooleanField(default = False)
    carroceria = models.ForeignKey(Carroceria, on_delete=models.PROTECT,related_name='solicitudes_carroceria_rel')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,related_name='solicitudes_usuario_rel')
    usuario_asignado = models.ForeignKey(User, on_delete=models.PROTECT,related_name='solicitudes_usuario_asignado_rel')
    ciudad_origen = models.ForeignKey(Ciudad, on_delete=models.PROTECT,related_name='solicitudes_ciudad_origen_rel')
    ciudad_destino = models.ForeignKey(Ciudad, on_delete=models.PROTECT,related_name='solicitudes_ciudad_destino_rel')
    
    class Meta:
        db_table = "gen_solicitud"