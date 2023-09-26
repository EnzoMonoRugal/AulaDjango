from typing import Any, Dict
from django import forms
from .models import *
from django.forms import ModelForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        widgets={
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'sexo' : forms.Select(attrs={'class':'form-control'}),
         }
    def clean_nome(self):
        nome = self.cleaned_data['nome']

        
        if len(nome) < 5:  
            raise forms.ValidationError('O nome deve ter pelo menos 5 caracteres.')

        return nome
