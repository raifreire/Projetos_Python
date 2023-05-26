from django import forms 

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Usuario:',
        required=True, 
        max_length=100,
        widget= forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Ex.: João Silva"
            }
        )
        
    )
    senha = forms.CharField(
        label='Senha:',
        required=True, 
        max_length=50,
        widget= forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"Digite sua senha"
            }
        )
    ) 

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro:",
        required=True,
        max_length=100,
        widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Ex.:João Silva"
            }
        )
    )
    email_cadastro = forms.EmailField(
        label="Email de Cadastro:",
        required=True,
        max_length=100,
        widget= forms.EmailInput({
            "class":"form-control",
            "placeholder":"Digite seu email"
            }
        )

    )
    senha = forms.CharField(
        label='Senha:',
        required=True, 
        max_length=50,
        widget= forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"Digite sua senha"
            }
        )
    ) 

    senha_check = forms.CharField(
        label='Check sua senha:',
        required=True, 
        max_length=50,
        widget= forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"Digite sua senha"
            }
        )
    ) 

