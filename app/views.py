from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.animal = request.POST.get('animal')
    novo_usuario.especie = request.POST.get('especie')
    novo_usuario.save()
    
    usuarios = {
    'usuarios': Usuario.objects.all()
    }
    
    return render(request, 'usuarios/usuarios.html',usuarios)