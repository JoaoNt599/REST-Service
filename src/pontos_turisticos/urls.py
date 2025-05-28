from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

     # Schema OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Documentação Swagger
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Documentação Redoc
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
