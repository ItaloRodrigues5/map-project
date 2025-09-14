from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .router.api import api_urls

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "api/",
        include(
            (api_urls, "myproject.router.api.api_urls"),
            namespace="api"
        ),
    ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),

    #path('vendas/<int:veiculo_id>/<int:cliente_id>/', views.registrar_venda, name='registrar_venda'),

    path('', views.index, name='index'),

    path('veiculos/', views.listar_veiculos, name='listar_veiculos'),
    path('veiculos/<int:veiculo_id>', views.detalhar_veiculo, name='detalhar_veiculo'),

    path('vendas/', views.listar_vendas, name='listar_vendas'),
    path('venda/new/', views.registrar_venda, name='registrar_venda'),
    path('venda/new/<int:veiculo_id>', views.registrar_venda, name='registrar_venda'),


    path('clientes/', views.listar_clientes, name='listar_clientes'),


]
