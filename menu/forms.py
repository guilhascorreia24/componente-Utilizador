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
            'ano': NumberInput(attrs={'class': 'input','min':2000}),
            'emaildiaaberto' : EmailInput(attrs={'class': 'input'}),
            'enderecopaginaweb': URLInput(attrs={'class': 'input'}),
            'datainscricaonasatividadesinicio': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datainscricaonasatividadesfim': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datadiaabertoinicio': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datadiaabertofim': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datapropostaatividadeinicio': DateInput(attrs={'class': 'input', 'type':'date'}),
            'datapropostaatividadesfim': DateInput(attrs={'class': 'input', 'type':'date'}),
            'preco_almoco_estudante': NumberInput(attrs={'class': 'input', 'value': '2.80', 'step': '0.01','min':0},),
            'preco_almoco_professor': NumberInput(attrs={'class': 'input', 'value': '4.20', 'step': '0.01','min':0}),
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
            'capacidade': NumberInput(attrs={'class': 'input','min':0}),
            'identificacao': TextInput(attrs={'class': 'input'}),
        }

class TransporteHorarioForm(ModelForm):
    horario_has_dia_id_dia_hora = forms.ModelChoiceField(queryset=HorarioHasDia.objects.all().order_by('horario_hora'))

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
                                    "rows": 0.5,
                                    'cols': 5,
                                }
                            )
                        )
    horario_has_dia_id_dia_hora = forms.ModelChoiceField(queryset=HorarioHasDia.objects.filter(horario_hora ='12:00:00'))
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
            'nralmocosdisponiveis': NumberInput(attrs={'class': 'input','min':0}),

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
            'nralmocos': NumberInput(attrs={'class': 'input','min':0}),
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


class InscricaoForm(forms.ModelForm):

    def save(self,id):
        base = super(InscricaoForm, self).save(commit=False)
        base.horario = TransporteHasHorario.objects.get(pk=id)
        return base.save()

    class Meta:
        model = TransporteHasInscricao
        exclude = ['transporte_has_inscricao_id','horario']
        widgets = {
            'n_passageiros': NumberInput(attrs={'class': 'input','min':0}),
        }

