from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "usuarios/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "usuarios/login.html", {
                "mensaje": "Credenciales no validas"
                })
    return render(request, "usuarios/login.html")
    
def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html", {
        "mensaje": "Ud. se ha desconectado."
        })
