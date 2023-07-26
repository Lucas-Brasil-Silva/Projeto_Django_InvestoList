from django.forms   import ModelForm
from .models   import Investimento

class Investimentoform(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'