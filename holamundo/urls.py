from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls), #ruta, template
    path('saludo/', views.saludo, name = 'saludo'), #por convencion se llama simpre a la vista igual a la url
    path('adulto/<int:edad>/', views.adulto, name = 'adulto'),
    path('simple/', views.simple, name = 'simple')
]
