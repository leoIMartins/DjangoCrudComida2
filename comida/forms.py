from django import forms
from comida.models import Comida


class ComidaForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['tipo', 'descricao', 'quantidade', 'opcoes', 'valorCalorico', 'salada']
        labels = {'tipo': 'Tipo', 'descricao': 'Descrição', 'quantidade': 'quantidade',
                  'opcoes': 'Opções', 'valorCalorico': 'Valor Calórico', 'quantidade': 'Quantidade'}
