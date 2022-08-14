from django.http import HttpResponse


from django.http import HttpResponse
from django.shortcuts import render

def saludo(request): #always recieve a request
    return HttpResponse("Hola mundo")

def adulto(request, edad): #en este ejemplo se recibe un parametro en la vista
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("No eres mayor de edad")

def simple(request):
    return render(request, 'simple.html', {}) 
    #información de la request, que plantilla, contexto (plantillas pueden necesitar datos)
    #en este caso es un contexto vacío

def dinamico(request, name):
    categories = ['code', 'design', 'mkt', 'business']
    context = {'name': name,
    'categories': categories}
    return render(request, 'dinamico.html', context)