from django import forms
from django.contrib.auth.models import User
from .models import Proposta, Empresa, Professor, Coordenador

class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class EmpresaForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )
    confirm_password = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'})
    )
    
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'endereco', 'email', 'telefone', 'whatsapp', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Empresa'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000000000000'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Endereço completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@empresa.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+5511987654321'}),
            'whatsapp': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações'}),
        }
        labels = {
            'nome': 'Nome da Empresa',
            'cnpj': 'CNPJ',
            'endereco': 'Endereço',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'whatsapp': 'Este número é WhatsApp?',
            'observacoes': 'Observações'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('As senhas não coincidem.')
        
        return cleaned_data


class ProfessorForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )
    confirm_password = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'})
    )
    
    class Meta:
        model = Professor
        fields = ['nome', 'matricula', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@professor.com'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'matricula': 'Matrícula',
            'email': 'E-mail'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('As senhas não coincidem.')
        
        return cleaned_data


class CoordenadorForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )
    confirm_password = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'})
    )
    
    class Meta:
        model = Coordenador
        fields = ['nome', 'matricula', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@coordenador.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+5511987654321'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'matricula': 'Matrícula',
            'email': 'E-mail',
            'telefone': 'Telefone'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('As senhas não coincidem.')
        
        return cleaned_data


class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = [
            'nomeSolucao',
            'tipoSistema',
            'objetivo',
            'tecnologias',
            'representante',
            'email',
            'telefone',
            'whatsapp',
            'expectativa',
            'vinculoIbmec'
        ]
        widgets = {
            'nomeSolucao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da solução'
            }),
            'tipoSistema': forms.Select(attrs={'class': 'form-control'}),
            'objetivo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o objetivo do projeto'
            }),
            'tecnologias': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ex: Python, Django, React, PostgreSQL'
            }),
            'representante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do representante'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+5511987654321'
            }),
            'whatsapp': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'expectativa': forms.Select(attrs={'class': 'form-control'}),
            'vinculoIbmec': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nomeSolucao': 'Nome da Solução',
            'tipoSistema': 'Tipo do Sistema',
            'objetivo': 'Objetivo do Projeto',
            'tecnologias': 'Tecnologias',
            'representante': 'Representante',
            'email': 'E-mail de Contato',
            'telefone': 'Telefone',
            'whatsapp': 'Este número é WhatsApp?',
            'expectativa': 'Expectativa de Entrega',
            'vinculoIbmec': 'Vínculo com IBMEC'
        }