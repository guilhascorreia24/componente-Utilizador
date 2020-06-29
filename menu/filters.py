# import django_filters
# from django_filters import DateFilter
# from .models import *

# class TransporteHorarioFilter(django_filters.FilterSet):
    
#     origem = django_filters.ChoiceFilter(choices = [("", "")] + [(par.paragem, par.paragem) for par in Paragem.objects.all()])

#     destino = django_filters.ChoiceFilter(choices = [("","")] +
# 	[(par.paragem, par.paragem) for par in Paragem.objects.all()])

    

#     class Meta:
#         model = TransporteHasHorario
#         fields = [
#             'horario_has_dia_id_dia_hora',
#         ]
#         exclude = ['capacidade']

# class DiaAbertoFilter(django_filters.FilterSet):
#     class Meta:
#         model = DiaAberto
#         fields = [
#             'ano',
#             'datadiaabertoinicio',
#             'datainscricaonasatividadesinicio',
#             'datapropostaatividadeinicio',
#         ]
#         exclude = ['']

# class MenuFilter(django_filters.FilterSet):
#     class Meta:
#         model = Menu
#         fields = [
#             'horario_has_dia_id_dia_hora',
#         ]
#         exclude = ['']