from rest_framework import viewsets, permissions
from general.models.solicitud import Solicitud
from general.serializers.solicitud import SolicitudSerializador

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializador    
    permission_classes = [permissions.IsAuthenticated]               