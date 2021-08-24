from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('suma/<int:numero1>/<int:numero2>/', views.sumar, name='sumar'),

    path('resta/<int:numero1>/<int:numero2>/', views.restar, name='restar'),

    path('multiplicacion/<int:numero1>/<int:numero2>/', views.multiplicar, name='multiplicar'),
    
    path('division/<int:numero1>/<int:numero2>/', views.dividir, name='dividir'),
]
