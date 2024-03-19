from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import minha_tarefa

def home(request):
    minha_tarefa.delay()
    return HttpResponse('Estou na home')