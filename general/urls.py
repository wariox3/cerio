from django.urls import path, include
from .views.prueba import PruebaView
from .views.solicitud import SolicitudViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'solicitud', SolicitudViewSet)

urlpatterns = [    
    path('', include(router.urls)),
    path('prueba/', PruebaView.as_view(), name='prueba'),
]