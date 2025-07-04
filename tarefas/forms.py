from django import forms
from .models import TarefaModel

class TarefasForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['nome', 'descricao', 'completo']