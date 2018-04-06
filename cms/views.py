from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages

# Create your views here.

def processRequest(request, recurso):
    if request.method == 'GET':
        try:
            objeto = Pages.objects.get(id = int(recurso))
            resp = objeto.page
        except Pages.DoesNotExist:
            resp = "objeto no contenido"
        return HttpResponse(resp)

def lista(request):
    list = Pages.objects.all()
    resp = "<ol>"
    for objeto in list:
        resp += '<li><a href="' + str(objeto.id) + '">' + objeto.name + '</a>'
    resp += "</ol>"
    return HttpResponse(resp)

def notOption(request, recurso):
    return HttpResponse("No contemplada esta opción.")
