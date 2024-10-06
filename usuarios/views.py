from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroFrom

def login(request):
  form = LoginForms()
  return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
  form = CadastroFrom()
  return render(request, 'usuarios/cadastro.html', {'form': form})
  