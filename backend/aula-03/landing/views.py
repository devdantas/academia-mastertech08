from django.shortcuts import render

# Create your views here.
def mostrar_index(req):
    return render(req, 'index.html')

def mostrar_sobre(req):
    return render(req, 'sobre.html')
