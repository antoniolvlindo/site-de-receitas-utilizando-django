from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Receitas</h1> <h2>Estas são as minhas receitas!</h2>')
