from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory,ValidationError
from django import forms
from inscricao import models
from inscricao.validators import email_validator, not_zero_validator, telefone_validator, SESSAO_MIN_ERROR

class Form_Responsaveis(ModelForm):

    def save(self, idinscricao):
        base = super(Form_Responsaveis, self).save(commit=False)
        base.idinscricao = idinscricao
        base.save()
        return base

    class Meta:
        model = models.Responsaveis
        fields = ['nome','email','telefone']

class Form_Inscricao(ModelForm):#numero de participantes precia de ser checkado
    turma = forms.CharField(max_length=1)
    participantes = forms.IntegerField(validators=[not_zero_validator])
    class Meta:
        model = models.Inscricao
        fields = ['ano','areacientifica','transporte']

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
        base = super(Form_Inscricao, self).save(commit=False)
        base.local = "Empty"
        base.save()
        query = models.InscricaoColetiva.objects.create(nresponsaveis = nresponsaveis, nparticipantes = self.cleaned_data['participantes'],participante_utilizador_idutilizador_id = idUtilizador.pk,escola_idescola = idEscola, inscricao_idinscricao = base, turma = self.cleaned_data['turma'])
        query.save()
        return base

class Form_Escola(ModelForm):

    class Meta:
        model = models.Escola
        fields = ['nome','local','telefone','email']

###################### TRANSPORTES ########################################

class Form_Transportes(ModelForm):

    def save(self, idinscricao):
        base = super(Form_Transportes, self).save(commit=False)
        base.inscricao_idinscricao = idinscricao
        print(self.cleaned_data["numero_passageiros"])
        base.save()
        return base

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
                form = Form_Prato(request.POST,prefix= "almoco_" + str(menu.idmenu),menu=menu)
                self.pratos.append((form,menu))

        else:
            for menu in menus:
                form = Form_Prato(prefix= "almoco_" + str(menu.idmenu),menu = menu)
                self.pratos.append((form,menu))
    
    def save(self,inscricao):
        for prato,menu in self.pratos:
            prat = prato.save()
            if prat.nralmocos>0:
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

    def __init__(self, *args, **kwargs):
        self.menu = kwargs.pop('menu')
        super(Form_Prato, self).__init__(*args, **kwargs)

    def save(self):
        base = super(Form_Prato, self).save(commit=False)
        base.menu_idmenu = self.menu
        if(base.nralmocos == 0):
            return base
        base.save()
        return base
    
    def clean(self):
        super().clean()
        if self.menu.nralmoçosdisponiveis < self.cleaned_data['nralmocos']:
            raise ValidationError({'nralmocos': ["Numero de almoços disponiveis não é suficiente"]})

        if(self.cleaned_data['nralmocos'] < 0):
            raise ValidationError({'nralmocos': ["Numero de almoços não pode ser negativo"]})

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
        sessao = models.Sessao.objects.get(idsessao=self.cleaned_data['sessao_id'])
        #print(sessao)
        base.sessao_idsessao = sessao
        base.save()
        return base

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data
        ids = cleaned_data['sessao_id']
        try:
            sessao = models.Sessao.objects.get(pk=ids)
        except models.Sessao.DoesNotExist:
            raise ValidationError("Sessão não existe")
       
        if sessao.capacidade - sessao.nrinscritos  < cleaned_data['nr_inscritos']:
            raise ValidationError({'nr_inscritos': ["Não há vagas suficientes"]})
        
        #return True
    class Meta:
        model = models.InscricaoHasSessao
        fields = ['nr_inscritos']

###################################################END SESSOES#############################################
class CustomForm:
    def __init__(self,request = 0):
        Sessao = modelformset_factory(models.InscricaoHasSessao,form = Form_Sessao,extra=0)
        Responsaveis = modelformset_factory(models.Responsaveis,form = Form_Responsaveis,extra=1)
        Transportes = modelformset_factory(models.TransporteHasInscricao,form = Form_Transportes,extra=0)
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
        print(self.sessao.is_valid())
        value = all([self.escola.is_valid(), self.inscricao.is_valid(), self.responsaveis.is_valid(), self.almoco.is_valid(),self.sessao.is_valid(),self.transportes.is_valid()])
        if len(self.sessao)<1:
            self.sessao.errors.append(SESSAO_MIN_ERROR)
            return False
        return value

    def save(self,part):

        escola = self.escola.save()
        inscricao = self.inscricao.save(part,escola,len(self.responsaveis))
        self.almoco.save(inscricao)

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