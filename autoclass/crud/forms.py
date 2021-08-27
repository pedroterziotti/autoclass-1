from django.forms import ModelForm, widgets
from .models import Aula



class NovaAulaForm(ModelForm):
    '''Classe de novo arquivo'''

    class Meta:
        model = Aula
       

        widgets = {
                "nome" : widgets.TextInput(attrs={"class": "form-control","style":"color:#ffffff"}),

                "plataforma" : widgets.Select(attrs={"class": "form-select","style":"color:#ffffff"}),

                "dia_da_aula": widgets.Select(attrs={"class": "form-select","style":"color:#ffffff"}),
    
                "horario_de_inicio": widgets.TimeInput({"class": "form-control","style":"color:#ffffff"}),

                "duracao_da_aula_minutos":widgets.NumberInput({"class": "form-select","style":"color:#ffffff"}) ,
               
                "link" : widgets.URLInput(attrs={"class": "form-select","style":"color:#ffffff"}),

                "login" : widgets.TextInput(attrs={"class": "form-control","style":"color:#ffffff"}),

                "senha": widgets.PasswordInput(attrs={"class": "form-control","style":"color:#ffffff"})
        }

        fields= '__all__'