from django.http import HttpResponse
from django.template import Context, Template, loader

def saludo(request):
    return HttpResponse("hola mundo")
def probando(request):
    nom='jose'
    ape='lopez'
    diccionario= {'nombre':nom,'apellido':ape}
    plantilla=loader.get_template('templates.html')
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)