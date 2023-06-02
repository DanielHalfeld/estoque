from django.forms import ModelForm, TextInput, Select
from .models import Saidas
class SaidaForm(ModelForm):
    class Meta:
        model = Saidas
        fields = ['produto', 'quantidade']
