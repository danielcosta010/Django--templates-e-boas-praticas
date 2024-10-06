from django import forms

class LoginForms(forms.Form):
  nome_login=forms.CharField(
    label='Nome de login',
    required=True,
    max_length=100
  )
  sennha=forms.CharField(
    label='Senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput()
  )