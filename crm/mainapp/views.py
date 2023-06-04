from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Django: The web framework for perfectionists with deadlines')

