from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from seguridad.views.seguridad import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/general/', include("general.urls")),
    path('api/seguridad/', include("seguridad.urls")),
    path('api/seguridad/login/', Login.as_view(), name='login'),
    path('api/seguridad/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/seguridad/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
