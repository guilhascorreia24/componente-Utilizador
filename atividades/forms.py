from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory
from django import forms
from atividades import models

class Form_Responsaveis(ModelForm):

    def save(self, idinscricao):
        base = super(Form_Responsaveis, self).save(commit=False)
        base.idinscricao = idinscricao
        return base.save()

    class Meta:
        model = models.Responsaveis
        fields = ['nome','email']

class Form_Inscricao(ModelForm):
    turma = forms.CharField(max_length=1)
    participantes = forms.IntegerField()
    class Meta:
        model = models.Inscricao
        fields = ['ano','local','areacientifica','transporte']

    def save(self, idUtilizador, idEscola, nresponsaveis):
        inscricao = super(Form_Inscricao, self).save(commit=True)
        query = models.InscricaoColetiva(nresponsaveis = nresponsaveis, nparticipantes = self.cleaned_data['participantes'],participante_utilizador_idutilizador = idUtilizador,escola_idescola = idEscola, inscricao_idinscricao = inscricao, turma = self.cleaned_data['turma'])
        query.save()
        return inscricao

class Form_Escola(ModelForm):
    class Meta:
        model = models.Escola
        fields = ['nome','local','telefone','email']

###################### TRANSPORTES ########################################

class Form_Transporte_Per_Campus(Form):
    numero_passageiros=forms.IntegerField(label="Numero de Passageiros")
    partida = forms.ModelChoiceField(queryset=models.HorarioHasDia.objects.all())
    chegada = forms.ModelChoiceField(queryset=models.HorarioHasDia.objects.all())

    def save(self,origem,inscricao,campus):
        destino = campus.paragem
        chegada = self.cleaned_data['partida']
        partida = self.cleaned_data['chegada']
        numero_passageiros = self.cleaned_data['numero_passageiros']
        db_partida = models.TransporteHasHorario(horario_has_dia_id_dia_hora = partida,npessoas=numero_passageiros,destino = destino,origem = origem)
        db_chegada = models.TransporteHasHorario(horario_has_dia_id_dia_hora = chegada,npessoas=numero_passageiros,destino = origem,origem = destino)
        db_transporte = models.TransporteHasInscricao(inscricao_idinscricao = inscricao,partida = db_partida, chegada = db_chegada)

        db_partida.save()
        db_chegada.save()
        db_transporte.save()


class Form_Transportes(Form):
    def __init__(self,request = 0):
        campus = models.Campus.objects.all()
        self.campus = list()
        if request != 0 and request.method == 'POST':
            for camp in campus:
                transporte = Form_Transporte_Per_Campus(request.POST,prefix="transporte_" + str(camp.idcampus))
                transporte.campus = camp
                self.campus.append(transporte)
        else:
            for camp in campus:
                transporte = Form_Transporte_Per_Campus(prefix="transporte_" + str(camp.idcampus))
                transporte.nome = camp.nome
                self.campus.append(transporte)

    def is_valid(self):
        value = True
        for camp in self.campus:
            if not camp.is_valid():
                value = False
        return value

    def save(self,origem,inscricao):
        for transporte in self.campus:
            transporte.save(origem,inscricao,transporte.campus)



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
        for prato,menu in self.pratos:
            prat = prato.save(menu)
            query = models.InscricaoHasPrato(inscricao_idinscricao = inscricao,prato_idprato=prat)
            query.save()

    def is_valid(self):
        value = True
        for prato,menu in self.pratos:
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
        base.save()
        return base

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
        self.almoco = Form_Almoco(request)
            self.inscricao = Form_Inscricao(request.POST,prefix="inscricao")

        else:
            self.escola = Form_Escola(prefix="escola")
            self.inscricao = Form_Inscricao(prefix="inscricao")
    
    def is_valid(self):
        return all([self.escola.is_valid(), self.inscricao.is_valid(), self.responsaveis.is_valid(), self.almoco.is_valid(),self.sessao.is_valid(),self.transportes.is_valid()])


        escola = self.escola.save()
        inscricao = self.inscricao.save(part,escola,len(self.responsaveis))
        self.almoco.save(inscricao)
        origem ,created = models.Paragem.objects.get_or_create(paragem = escola.local)
        self.transportes.save(origem,inscricao)

        for each in self.sessao:
            each.save(inscricao)
        
        
        for each in self.responsaveis:
            each.save(inscricao)
        return self


#TEMPLATE

# - form
#   - inscricao
#   - escola
#   - sessao
#   - responsaveis
#   - almoco
#       - campus (array)
#           - nome (nome do campus)
#           - (prato,menu) (array de tuppples)
#   - transporte
#       -campus (array)
#           - nome  (nome do campus)
#           - transporte
#           
#
#
#
#
#
#