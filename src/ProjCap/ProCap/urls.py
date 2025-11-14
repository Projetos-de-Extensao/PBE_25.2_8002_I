from django.contrib import admin
from django.urls import path, include
from . import views
from cadastro import views as cadastro_views
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Conteúdos",
        default_version='v1',
        description="Documentação da API para o app de streaming de áudio e vídeo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suporte@exemplo.com"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cadastro_views.escolher_tipo_cadastro, name='escolher_cadastro'),
    path('cadastro/', cadastro_views.cadastro, name='cadastro_empresa'),
    path('cadastro/empresa/', cadastro_views.cadastro_empresa, name='cadastro_empresa_form'),
    path('cadastro/professor/', cadastro_views.cadastro_professor, name='cadastro_professor'),
    path('cadastro/coordenador/', cadastro_views.cadastro_coordenador, name='cadastro_coordenador'),
    path('login/', cadastro_views.login_view, name='login'),
    path('logout/', cadastro_views.logout_view, name='logout'),
    path('dashboard/', cadastro_views.dashboard, name='dashboard'),
    path('dashboard/professor/', cadastro_views.dashboard_professor, name='dashboard_professor'),
    path('dashboard/coordenador/', cadastro_views.dashboard_coordenador, name='dashboard_coordenador'),
    path('proposta/nova/', cadastro_views.criar_proposta, name='criar_proposta'),
    path('proposta/<int:proposta_id>/editar/', cadastro_views.editar_proposta, name='editar_proposta'),
    path('proposta/<int:proposta_id>/alterar-status/', cadastro_views.alterar_status_proposta, name='alterar_status_proposta'),
    path('proposta/<int:proposta_id>/designar-professor/', cadastro_views.designar_professor, name='designar_professor'),
    path('perfil/editar/', cadastro_views.editar_perfil, name='editar_perfil'),
    path('api/', include('cadastro.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]