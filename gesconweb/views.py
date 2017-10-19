#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http import HttpResponse

import datetime
import os

from django.contrib.auth.models import Group
from .models import Aplicativo, Permiso

# Create your views here.


def homepage(request):
    apps = list(
        Aplicativo.objects
        .prefetch_related('permiso_set')
        .all()
        )
    return render(request, 'gesconweb/homepage.html', {
        'apps': apps,
        }) 


def detalle_aplicativo(request, id_app):
    id_app = int(id_app)
    app = Aplicativo.objects.get(pk=id_app)
    grupos = [p.grupo for p in Permiso.objects
        .select_related('grupo')
        .filter(aplicativo=app)
        .order_by('orden')
        ]
    
    return render(request, 'gesconweb/detalle_aplicativo.html', {
        'aplicativo': app,
        'grupos': grupos,
        })

def lista_grupos(request):
    grupos = Group.objects.all().order_by('name')
    grupos = grupos.select_related('permiso_set')
    return render(request, 'gesconweb/lista_grupos.html', {
        'grupos': grupos, 
        })

def hola(request, numeros, letras):
    return HttpResponse('Matrícula (<i>normalizada</i>): <b><tt>{}{}</tt></b>'.format(
        numeros,
        letras.upper(),
        )
        )
