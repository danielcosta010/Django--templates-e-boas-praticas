from django import forms

class LoginForms(forms.Form):
  nome_login=forms.CharField(
    label='Nome de login',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite seu usuario',
      }
    )
  )
  senha=forms.CharField(
    label='Senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha',
      }
    )
  )

class CadastroFrom(forms.Form):
  nome_usuario=forms.CharField(
    label='Nome de usuario',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite seu usuario',
      }
    )
  )
  email=forms.EmailField(
    label='Email',
    required=True,
    max_length=100,
    widget=forms.EmailInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite seu email',
      }
    )
  )
  senha=forms.CharField(
    label='Senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha',
      }
    )
  )
  repita_senha=forms.CharField(
    label='Repita sua Senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha novamente',
      }
    )
  )

  def clean_nome_usuario(self):
    nome = self.cleaned_data.get('nome_usuario')
    if nome:
      nome = nome.strip()
      if ' ' in nome:
        raise forms.ValidationError('O nome de usuário não pode conter espaços')
      else:
        return nome
