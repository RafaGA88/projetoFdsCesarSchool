from django.shortcuts import redirect, render
from .models import Usuario
from django.core.validators import validate_email #Validar email

def index(request):
    return render(request, 'usuario/login.html')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'usuario/cadastro.html')

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    nomeConsulta = Usuario.objects.raw(f'SELECT * FROM usuario_Usuario WHERE nome = {nome}')
    emailConsulta = Usuario.objects.raw(f'SELECT * FROM usuario_Usuario WHERE email = {email}')

    if nome == nomeConsulta:
        return render(request, 'usuario/cadastro.html')#Já existe
    
    if email == emailConsulta:
        return render(request, 'usuario/cadastro.html')#Já existe

    if not nome or not email or not senha:
        return render(request, 'usuario/cadastro.html')#Se estiver em branco
    
    if len(senha) < 6:
        return render(request, 'usuario/cadastro.html')#Se a senha tiver menos que 6 caracteres
    
    #Validação de email
    try:   
        validate_email(email)
    except:
        return render(request, 'usuario/cadastro.html')

    usuario = Usuario(nome=nome, email=email, senha=senha) #variável da esquerda é do bd e da direita é as de cima
    usuario.save() #salvar no banco de dados

    return redirect('login')