from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Respuestas")

def sumar(request, numero1, numero2):
    return HttpResponse("La suma es: " + str(numero1 + numero2))

def restar(request, numero1, numero2):
    return HttpResponse("La resta es: " + str(numero1 - numero2))

def multiplicar(request, numero1, numero2):
    return HttpResponse("La multiplicacion es: " + str(numero1 * numero2))

def dividir(request, numero1, numero2):
    return HttpResponse("La division es: " + str(numero1 / numero2))