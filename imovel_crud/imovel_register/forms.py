from django import forms
from .models import Imovel

class ImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = ('tipo', 'area', 'endereco', 'cep', 'position')
        labels = {
            'tipo': 'Tipo de imóvel',
            'area': 'Área(m²)',
            'endereco': 'Endereço',
            'cep': 'CEP',
            'position': 'Finalidade'
        }

    def __init__(self, *args, **kwargs):
         super(ImovelForm, self).__init__(*args, **kwargs)
         self.fields['position'].empty_label = "Select"
         self.fields['area'].required = False