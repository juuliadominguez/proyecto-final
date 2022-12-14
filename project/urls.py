"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ejemplo.views import (index, saludar_a, sumar, buscar, mostrar_familiares, mostrar_perros, mostrar_gatos,
                           BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar,
                           BuscarGatos, AltaGatos, ActualizarGatos, BorrarGatos, 
                           BuscarPerros, AltaPerros, ActualizarPerros, BorrarPerros)


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('saludar/', index),
    #path('saludar-a/<nombre>/', saludar_a),
    #path('sumar/<int:a>/<int:b>/', sumar),
    #path('buscar/', buscar),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mis-gatos/', mostrar_gatos),
    path('mis-gatos/buscar', BuscarGatos.as_view()),
    path('mis-gatos/alta', AltaGatos.as_view()),
    path('mis-gatos/actualizar/<int:pk>', ActualizarGatos.as_view()),
    path('mis-gatos/borrar/<int:pk>', BorrarGatos.as_view() ),
    path('mis-perros/', mostrar_perros),
    path('mis-perros/buscar',BuscarPerros.as_view()),
    path('mis-perros/alta', AltaPerros.as_view()),
    path('mis-perros/actualizar/<int:pk>', ActualizarPerros.as_view()),
    path('mis-perros/borrar/<int:pk>', BorrarPerros.as_view())

]
