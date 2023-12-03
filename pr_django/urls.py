"""
URL configuration for pr_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quimun.api.views import ClienteApiViewSet, ClienteID, ClientesPorApellido, EmpresaApiViewSet, ArriendoApiViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clientes/', ClienteApiViewSet.as_view({'get': 'list', 'post': 'create'}), name='cliente-list'),
    path('api/cliente-id/<int:id>/', ClienteID.as_view(), name='cliente-detail'),
    path('api/clientes-por-apellido/', ClientesPorApellido.as_view(), name='clientes-por-apellido'),
    path('api/empresas/', EmpresaApiViewSet.as_view({'get': 'list', 'post': 'create'}), name='empresa-list'),
    path('api/arriendos/', ArriendoApiViewSet.as_view({'get': 'list', 'post': 'create'}), name='arriendo-list'),
    # path('api/arriendos-ordenados-costo-diario/', ArriendoPorGasto.as_view, name='arriendos-ordenados-costo-diario'),
]


