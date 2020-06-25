from django.forms import *
from django import forms
from .models import *

##### Dia Aberto #####


class DiaAbertoForm(ModelForm):
    descricao = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Descrição",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    class Meta:
        model = DiaAberto
        exclude = ['administrador_utilizador_idutilizador']
        widgets = {
            'ano': TextInput(attrs={'class': 'input'}),
            'emaildiaaberto' : EmailInput(attrs={'class': 'input'}),
            'enderecopaginaweb': URLInput(attrs={'class': 'input'}),
            'datainscricaonasatividadesinicio': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datainscricaonasatividadesfim': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datadiaabertoinicio': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datadiaabertofim': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datapropostaatividadeinicio': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datapropostaatividadesfim': DateInput(attrs={'class': 'input', 'type':'date'}),
            'preco_almoco_estudante': NumberInput(attrs={'class': 'input', 'value': '2.80', 'step': '0.01'}),
            'preco_almoco_professor': NumberInput(attrs={'class': 'input', 'value': '4.20', 'step': '0.01'}),
        }

### Transporte ####
class TransportForm(ModelForm):
    class Meta:
        model = Transporte
        fields = [
            'idtransporte',
            'capacidade',
            'identificacao',
        ]
        widgets = { 
            'capacidade': NumberInput(attrs={'class': 'input'}),
            'identificacao': TextInput(attrs={'class': 'input'}),
        }

class TransporteHorarioForm(ModelForm):

    class Meta:
        model = TransporteHasHorario
        fields = [
            'origem',
            'destino',
            'horario_has_dia_id_dia_hora',
        ]
        exclude = [
            'transporte_idtransporte',
            'n_passageiros',

        ]

### Menu ####
class MenuModelForm(forms.ModelForm):
    descricao = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Sopa e Sobremesa",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 2,
                                    'cols': 10,
                                }
                            )
                        )
    class Meta:
        model = Menu
        fields = [
            'idmenu',
            'menu',
            'descricao',
            'campus_idcampus',
            'horario_has_dia_id_dia_hora',
            'nralmocosdisponiveis',
            ]
        widgets = {
            'menu': TextInput(attrs={'class': 'input', 'value': 'Menu do dia'}),
            'nralmocosdisponiveis': NumberInput(attrs={'class': 'input'}),
        }

class MenuPrecoForm(forms.ModelForm):
    class Meta:
        model = DiaAberto
        fields = [
            'preco_almoco_estudante',
            'preco_almoco_professor'

        ]

class PratoForm(forms.ModelForm):
    descricao = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Descrição",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 10,
                                    'cols': 40,
                                }
                            )
                        )

    class Meta:
        model = Prato
        
        fields = [
            'idprato', 
            'tipo', 
            'descricao',
            'nralmocos', 
            'menu_idmenu', 
        ]

        widgets = {
            'nralmocos': NumberInput(attrs={'class': 'input'}),
        }



class HoraForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'hora',
        ]
        widgets = {
            'hora': TimeInput(attrs={'class': 'input', 'type':'time'}),
        }

class DiaForm(forms.ModelForm):
    class Meta:
        model = Dia
        fields = [
            'dia',
        ]

        widgets = {
            'dia': DateInput(attrs={'class': 'input', 'type':'date'}),
        }

class HorarioForm(forms.ModelForm):
    class Meta:
        model = HorarioHasDia
        fields = [
            'horario_hora',
            'dia_dia',
            'id_dia_hora',
        ]

        widgets = {
            'horario_hora': TimeInput(attrs={'class': 'input', 'type':'time'}),
            'dia_dia': DateInput(attrs={'class': 'input', 'type':'date'}),
        }

class InscricaoForm(forms.Form):
    n_passageiros = IntegerField()
    inscricao_idinscricao = ModelChoiceField(Inscricao.objects)
    def save(self,id):
        base = TransporteHasInscricao(n_passageiros=self.cleaned_data['n_passageiros'],inscricao_idinscricao=self.cleaned_data['inscricao_idinscricao'], horario=TransporteHasHorario.objects.get(id))
        return base.save()
