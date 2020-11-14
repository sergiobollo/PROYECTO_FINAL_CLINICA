from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"clinica/index.html", { "titulo": "Bienvenidos a nuestra clínica de Optometría"})