from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

        usuario = auth.authenticate(
            request,
            username = nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request,f"Olá {nome} !")
            return redirect('index')
        else:
            messages.error(request, "erro ao efetuar login")
            return redirect('login')    

    return render(request, "usuarios/login.html",{"form":form} )

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha"].value() != form["senha_check"].value():
                messages.error(request, "As senhas não são identicas")
                return redirect('cadastro')
            
            nome = form["nome_cadastro"].value()
            email = form["email_cadastro"].value()
            senha = form["senha"].value()
            # print(nome, email, senha)

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuario já existente")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email= email,
                password=senha
            )

            usuario.save()
            messages.success(request, f"usuario {nome} criado com sucesso!")
            return redirect('login')

    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso !")
    return redirect('login')
