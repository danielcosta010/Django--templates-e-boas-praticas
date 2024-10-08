from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroFrom
from django.contrib.auth.models import User

def login(request):
  form = LoginForms()
  return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
  form = CadastroFrom()
  if request.method == 'POST':
    form = CadastroFrom(request.POST)
    
    if form.is_valid():
      if form['senha'].value() != form['repita_senha'].value():
        return redirect('cadastro')
      
      nome = form['nome_usuario'].value()
      email = form['email'].value()
      senha = form['senha'].value()

      if User.objects.filter(username=nome).exists():
        return redirect('cadastro')
      
      usuario = User.objects.create_user(
        username=nome,
        email=email,
        password=senha
      )
      usuario.save()
      return redirect('login')



  return render(request, 'usuarios/cadastro.html', {'form': form})
  