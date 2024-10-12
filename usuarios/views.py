from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroFrom
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
  form = LoginForms()

  if request.method == 'POST':
    form = LoginForms(request.POST)

    if form.is_valid():
      nome = form['nome_login'].value()
      senha = form['senha'].value()

    usuario = auth.authenticate(
      request,
      username=nome,
      password=senha
    )
    if usuario is not None:
      auth.login(request, usuario)
      messages.success(request, f'{nome} logado com sucesso')
      return redirect('index')
    else:
      messages.error(request, 'Login ou senha inválidos')
      return redirect('login')

  return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
  form = CadastroFrom()

  if request.method == 'POST':
    form = CadastroFrom(request.POST)
    
    if form.is_valid():
            
      nome = form['nome_usuario'].value()
      email = form['email'].value()
      senha = form['senha'].value()

      if User.objects.filter(username=nome).exists():
        messages.error(request, 'Usuario já existe')
        return redirect('cadastro')
      
      usuario = User.objects.create_user(
        username=nome,
        email=email,
        password=senha
      )
      usuario.save()
      messages.success(request, 'Usuário cadastrado com sucesso')
      return redirect('login')



  return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
  auth.logout(request)
  messages.success(request, 'Logout efetuado com sucesso')
  return redirect('login')  