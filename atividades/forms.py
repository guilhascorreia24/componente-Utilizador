from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory
from django import forms
from atividades import models


class Form_Create_Atividades(ModelForm):
    class Meta:
        model = models.Atividade
        fields = ['titulo','capacidade','duracao','descricao','espaco_idespaco']
    
class Form_Responsaveis(ModelForm):

    def save(self, idinscricao):
        base = super(Form_Responsaveis, self).save(commit=False)
        base.idinscricao = idinscricao
        return base.save()

    class Meta:
        model = models.Responsaveis
        fields = ['nome','email']

class Form_Inscricao(ModelForm):
    class Meta:
        model = models.Inscricao
        fields = ['ano','local','areacientifica']

class Form_InscricaoColetiva(ModelForm):
    def save(self, idUtilizador, idEscola, idInscricao):
        base = super(Form_InscricaoColetiva, self).save(commit=False)
        base.participante_utilizador_idutilizador= idUtilizador
        base.escola_idescola = idEscola
        base.inscricao_idinscricao = idInscricao
        return base.save()

    class Meta:
        model = models.InscricaoColetiva
        fields = ['turma']

class Form_Escola(ModelForm):
    class Meta:
        model = models.Escola
        fields = ['nome','local','telefone','email']


class Form_Transportes(Form):
    numero_transportes_penha=forms.IntegerField(label="Penha Numero de Passageiros")
    numero_transportes_gambleas = forms.IntegerField(label="Gambelas Numero de Passageiros")
    partida = forms.ModelChoiceField(queryset=models.HorarioHasDia.objects.all())
    chegada = forms.ModelChoiceField(queryset=models.HorarioHasDia.objects.all())

    def save(self, inscricao, escola):
        paragem = models.Paragem(paragem=escola.local)  #Testar para varias inscrições da mesma escola

        #if numero_transportes_penha >= 0:  
        #    transporteHasHorario_penha = models.TransporteHasHorario(origem,destino,horario_partida,num)
        #    transporteHasHorario__penha_1 = models.TransporteHasHorario(destino,origem,horario_chegada,num)
        #    transporteHasInscricao = models.TransporteHasInscricao(inscricao_idinscricao = inscricao,partida = transporteHasHorario__penha_1,chegada = transporteHasHorario_penha)

        #f numero_transportes_gambelas >= 0:
        #    transporteHasHorario_gambelas = models.TransporteHasHorario(origem,destino,horario_partida,num)
        #    transporteHasHorario_gambelas_1 = models.TransporteHasHorario(destino,origem,horario_chegada,num)
        #    transporteHasInscricao = models.TransporteHasInscricao(inscricao_idinscricao = inscricao,partida = transporteHasHorario__penha_1,chegada = transporteHasHorario_penha)

########################Almoços###########################
class Form_Almocos_Per_Campus:
    def __init__(self,campus,request = 0):
        self.nome = campus.nome
        self.pratos = list()
        menus = models.Menu.objects.filter(campus_idcampus = campus)
        if request != 0 and request.method == 'POST':
            for menu in menus:
                form = Form_Prato(request.POST,prefix= "almoco_" + str(menu.idmenu))
                self.pratos.append((form,menu))

        else:
            for menu in menus:
                form = Form_Prato(prefix= "almoco_" + str(menu.idmenu))
                self.pratos.append((form,menu))
    
    def save(self,inscricao):
        for (prato,menu) in self.pratos:
            prat = prato.save(menu)
            models.InscricaoHasPrato(inscricao_idinscricao = inscricao,prato_idprato=prat)

    def is_valid(self):
        value = True
        for (prato,menu) in self.pratos:
            if not prato.is_valid():
                value = False
        return value
    
#Save method doesn't return
class Form_Almoco:
    def __init__(self,request):
        campus = models.Campus.objects.all()
        self.campus = list()
        for camp in campus:
            self.campus.append(Form_Almocos_Per_Campus(camp,request))
    
    def is_valid(self):
        value = True
        for c in self.campus:
            if not c.is_valid():
                value = False
        return value

    def save(self,inscricao):
        for c in self.campus:
            c.save(inscricao) 


        
class Form_Prato(ModelForm):

    def set_menu(self,menu):
        self.menu = menu
    def save(self,menu):
        base = super(Form_Prato, self).save(commit=False)
        base.menu_idmenu = menu
        return base.save()

    class Meta:
        model = models.Prato
        fields = ['nralmocos']
###################################################END ALMOÇO #########################################

###################################################SESSOES#############################################

class Form_Sessao(ModelForm):

    class Meta:
        model = models.Prato
        fields = ['sessao_idsessao','inscritos']

###################################################END SESSOES#############################################
class CustomForm:
    def __init__(self,request = 0):
        self.responsaveis = modelformset_factory(models.Responsaveis,form = Form_Responsaveis,extra=2)
        self.almoco = Form_Almoco(request)
        if request != 0 and request.method == 'POST':
            self.escola = Form_Escola(request.POST,prefix="escola")
            self.inscricao = Form_Inscricao(request.POST,prefix="inscricao")
            self.inscricao_coletiva = Form_InscricaoColetiva(request.POST,prefix="coletivo")
            self.responsaveis = self.responsaveis(request.POST)
        else:
            self.escola = Form_Escola(prefix="escola")
            self.inscricao = Form_Inscricao(prefix="inscricao")
            self.inscricao_coletiva = Form_InscricaoColetiva(prefix="coletivo")
    
    def is_valid(self):
        return all([self.escola.is_valid(), self.inscricao.is_valid(), self.responsaveis.is_valid(), self.almoco.is_valid()])#self.inscricao_coletiva.is_valid())

    def save(self):
        escola = self.escola.save()
        inscricao = self.inscricao.save()
        self.almoco.save(inscrciao)
        
        for each in self.responsaveis:
            each.save(inscricao)
        return self


#TEMPLATE

# - form
#   - inscricao
#   - escola
#   - almoco
#       - campus
#           - nome
#           - (prato,menu)
#
#
#
#
#
#