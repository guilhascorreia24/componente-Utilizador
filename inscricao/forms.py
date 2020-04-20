from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory,ValidationError
from django import forms
from inscricao import models

class Form_Responsaveis(ModelForm):

    def save(self, idinscricao):
        base = super(Form_Responsaveis, self).save(commit=False)
        base.idinscricao = idinscricao
        return base.save()

    class Meta:
        model = models.Responsaveis
        fields = ['nome','email','telefone']

class Form_Inscricao(ModelForm):
    turma = forms.CharField(max_length=1)
    participantes = forms.IntegerField()
    class Meta:
        model = models.Inscricao
        fields = ['ano','areacientifica','transporte']
    
    def save(self):
        base = super(Form_Inscricao, self).save(commit=False)
        base.local = "Empty"
        return base.save()

    transporte = forms.ChoiceField(
    initial=(0,'Não'),
    required=True,
    widget=forms.RadioSelect,
    choices=(
        (0,'Não'),
        (1,'Sim'),
    )
)

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

class Form_Transportes(ModelForm):

    def save(self, idinscricao):
        base = super(Form_Transportes, self).save(commit=False)
        base.inscricao_idinscricao = idinscricao
        return base.save()

    class Meta:
        model = models.TransporteHasInscricao
        fields = ['partida','numero_passageiros','partida_paragem','chegada_paragem']


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
    sessao_id = forms.IntegerField()


    def save(self,inscricao):
        base = super(Form_Sessao, self).save(commit=False)
        base.inscricao_idinscricao = inscricao
        base.sessao_idsessao = self.cleaned_data['sessao_id']
        return base.save()

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data
        ids = cleaned_data['sessao_id']
        try:
            sessao = models.Sessao.objects.get(pk=ids)
        except models.Sessao.DoesNotExist:
            raise ValidationError("Sessão não existe")
       
        if cleaned_data['nrinscritos'] > sessao.vagas:
           raise ValidationError("Sessão não têm vagas suficientes")
        
        #return True
    class Meta:
        model = models.InscricaoHasSessao
        fields = ['nrinscritos']

###################################################END SESSOES#############################################
class CustomForm:
    def __init__(self,request = 0):
        Sessao = modelformset_factory(models.InscricaoHasSessao,form = Form_Sessao,extra=0)
        Responsaveis = modelformset_factory(models.Responsaveis,form = Form_Responsaveis,extra=1)
        Transportes = modelformset_factory(models.TransporteHasInscricao,form = Form_Transportes,extra=1)
        self.almoco = Form_Almoco(request)
        if request != 0 and request.method == 'POST':
            self.escola = Form_Escola(request.POST,prefix="escola")
            self.inscricao = Form_Inscricao(request.POST,prefix="inscricao")
            self.responsaveis = Responsaveis(request.POST,prefix='responsaveis_set')
            self.sessao = Sessao(request.POST,prefix='sessao_set')
            self.transportes = Transportes(request.POST,prefix='transportes_set')
        else:
            self.escola = Form_Escola(prefix="escola")
            self.inscricao = Form_Inscricao(prefix="inscricao")
            self.sessao = Sessao(prefix='sessao_set',queryset=models.InscricaoHasSessao.objects.none())
            self.responsaveis = Responsaveis(prefix='responsaveis_set',queryset=models.Responsaveis.objects.none())
            self.transportes = Transportes(prefix='transportes_set',queryset=models.TransporteHasInscricao.objects.none())
    
    def is_valid(self):
        print(self.inscricao.is_valid())
        return all([self.escola.is_valid(), self.inscricao.is_valid(), self.responsaveis.is_valid(), self.almoco.is_valid(),self.sessao.is_valid(),self.transportes.is_valid()])

    def save(self):
        user = models.Utilizador.objects.get(idutilizador = 42)
        part = models.Participante.objects.get(utilizador_idutilizador = user)

        escola = self.escola.save()
        inscricao = self.inscricao.save(part,escola,len(self.responsaveis))
        self.almoco.save(inscricao)
        origem ,created = models.Paragem.objects.get_or_create(paragem = escola.local)

        for each in self.transportes:
            each.save(inscricao)


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
#   - transportes
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