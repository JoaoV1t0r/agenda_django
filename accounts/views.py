import accounts
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    confirma_senha = request.POST.get('confirma_senha')

    if not nome or not email or not senha or not confirma_senha:
        messages.error(request, 'Nenhum campo poder estar vazio')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido')
        return render(request, 'accounts/register.html')

    if len(nome) < 6:
        messages.error(request, 'Nome precisa ter no mínimo 6 caracteres')
        return render(request, 'accounts/register.html')

    if len(senha) < 4:
        messages.error(request, 'Senha precisa ter no mínimo 4 caracteres')
        return render(request, 'accounts/register.html')

    if senha != confirma_senha:
        messages.error(request, 'As senha são diferentes, tente novamente')
        return render(request, 'accounts/register.html')

    exists = User.objects.filter(email=email)
    if exists:
        messages.error(request, 'E-mail já cadastrado')
        return render(request, 'accounts/register.html')

    user = User.objects.create_user(username=nome, email=email, password=senha)
    user.save()
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
