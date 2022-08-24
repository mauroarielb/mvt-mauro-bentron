from django.shortcuts import render
from .models import familia
from django.template import context,Template,loader
from django.http import HttpResponse

def familiar(request):
    familiar1=familia(nombre='pedro', edad='25', fecha_nacimiento='1997-2-11')
    familiar2=familia(nombre='jose', edad='20', fecha_nacimiento='2002-3-6')
    familiar3=familia(nombre='jorge', edad='24', fecha_nacimiento='1998-4-17')
    diccionario={'nombre1':familiar1.nombre, 'edad1':familiar1.edad, 'fecha_nacimiento1':familiar1.fecha_nacimiento,
    'nombre2':familiar2.nombre, 'edad2':familiar2.edad, 'fecha_nacimiento2':familiar2.fecha_nacimiento,
    'nombre3':familiar3.nombre, 'edad3':familiar3.edad, 'fecha_nacimiento3':familiar3.fecha_nacimiento }
   
    plantilla=loader.get_template('templates.html')
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)
  
