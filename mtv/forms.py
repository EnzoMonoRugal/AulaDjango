from typing import Any, Dict
from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "email", "sexo"]
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']

        
        if len(nome) < 5:  
            raise forms.ValidationError('O nome deve ter pelo menos 5 caracteres.')

        return nome
