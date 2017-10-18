#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http import HttpResponse

import datetime
import os

# Create your views here.


def homepage(request):
    return render(request, 'gesconweb/homepage.html', {
        'now': datetime.datetime.now(),
        'ficheros': os.listdir('/home/'),
        }) 

def hola(request, numeros, letras):
    return HttpResponse('Matrícula (<i>normalizada</i>): <b><tt>{}{}</tt></b>'.format(
        numeros,
        letras.upper(),
        )
        )
