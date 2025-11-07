from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PropostaViewSet, ProjetoViewSet, CoordenadorViewSet, ProfessorViewSet, EmpresaViewSet

router = DefaultRouter()
router.register('propostas', PropostaViewSet)
router.register('projetos', ProjetoViewSet)
router.register('coordenadores', CoordenadorViewSet)
router.register('professores', ProfessorViewSet)
router.register('empresas', EmpresaViewSet)

urlpatterns = router.urls