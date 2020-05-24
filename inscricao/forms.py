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

class Form_InscricaoColetiva(ModelForm):
    def save(self, idUtilizador, idEscola, nresponsaveis, inscricao):
        base = super(Form_InscricaoColetiva, self).save(commit=False)
        base.local = "Empty"
        base.nresponsaveis = nresponsaveis
        base.participante_utilizador_idutilizador_id = idUtilizador.pk
        base.escola_idescola = idEscola
        base.inscricao_idinscricao = inscricao
        base.save()
        return base

    class Meta:
        model = models.InscricaoColetiva
        fields = ['nparticipantes','turma']

class Form_Inscricao(ModelForm):#numero de participantes precia de ser checkado

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

    def save(self):
        base = super(Form_Inscricao, self).save(commit=False)
        base.local = "Empty"
        base.save()
        return base

class Form_Escola(ModelForm):

    class Meta:
        model = models.Escola
        fields = ['nome','local','telefone','email']

###################### TRANSPORTES ########################################

#Cannot be null
#Check if is full
class Form_Transportes(ModelForm):
    def save(self, idinscricao):
        base = super(Form_Transportes, self).save(commit=False)
        base.inscricao_idinscricao = idinscricao
        base.save()
        return base

    class Meta:
        model = models.TransporteHasInscricao
        fields = ['horario','n_passageiros']


########################Almoços###########################

class Form_Almocos_Per_Campus:
    def __init__(self,campus,request = 0,**kwargs):
        self.nome = campus.nome
        self.pratos = list()
        if 'instance' in kwargs:
            self.curr_insc = kwargs['instance']
        else:
            self.curr_insc = None

        menus = models.Menu.objects.filter(campus_idcampus = campus)
        if request != 0 and request.method == 'POST':
            #Preciso para quando é necessária uma alteração no numero
            if self.curr_insc != None:
                pratos = models.InscricaoHasPrato.objects.select_related('prato_idprato').filter(inscricao_idinscricao=self.curr_insc)
            else:
                pratos = []
            for menu in menus:

                found = None
                for x in pratos:
                    if x.prato_idprato.menu_idmenu.pk == menu.pk:
                        found = x
                        break

                if found != None:
                    form = Form_Prato(request.POST,prefix= "almoco_" + str(menu.idmenu),menu=menu,instance=found.prato_idprato)
                else:
                    form = Form_Prato(request.POST,prefix= "almoco_" + str(menu.idmenu),menu=menu)
                self.pratos.append((form,menu))

        else:
            if self.curr_insc != None:
                pratos = models.InscricaoHasPrato.objects.select_related('prato_idprato').filter(inscricao_idinscricao=self.curr_insc)
            else:
                pratos = []
            for menu in menus:
                found = None
                for x in pratos:
                    if x.prato_idprato.menu_idmenu.pk == menu.pk:
                        found = x
                        break

                if found != None:
                    form = Form_Prato(prefix= "almoco_" + str(menu.idmenu),menu=menu,instance=found.prato_idprato)
                else:
                    form = Form_Prato(prefix= "almoco_" + str(menu.idmenu),menu=menu)

                self.pratos.append((form,menu))
    
    #Bug when change is requested, and one entry is set to 0
    def save(self,inscricao):
        for prato,menu in self.pratos:
            prat = prato.save()
            if prat.nralmocos>0:
                if not models.InscricaoHasPrato.objects.filter(prato_idprato=prat).exists():
                    query = models.InscricaoHasPrato(inscricao_idinscricao = inscricao,prato_idprato=prat)
                    query.save()
            else:
                model =  models.InscricaoHasPrato.objects.filter(prato_idprato=prat).delete()
                    

    def is_valid(self):
        value = True
        for prato,menu in self.pratos:
            if not prato.is_valid():
                value = False
        return value
    
#Save method doesn't return
class Form_Almoco:
    def __init__(self,request,**kwargs):
        campus = models.Campus.objects.all()
        self.campus = list()
        for camp in campus:
            self.campus.append(Form_Almocos_Per_Campus(camp,request,**kwargs))
    
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
        if self.menu.nralmocosdisponiveis < self.cleaned_data['nralmocos']:
            raise ValidationError({'nralmocos': ["Numero de almoços disponiveis não é suficiente"]})

        if(self.cleaned_data['nralmocos'] < 0):
            raise ValidationError({'nralmocos': ["Numero de almoços não pode ser negativo"]})

    class Meta:
        model = models.Prato
        fields = ['nralmocos']
###################################################END ALMOÇO #########################################

###################################################SESSOES#############################################

class Form_Sessao(ModelForm):
    #sessao_id = forms.IntegerField()


    def save(self,inscricao):
        base = super(Form_Sessao, self).save(commit=False)
        base.inscricao_idinscricao = inscricao
        #sessao = models.Sessao.objects.get(idsessao=self.cleaned_data['sessao_idsessao'])
        #base.sessao_idsessao = sessao
        base.save()
        return base

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data
        ids = cleaned_data['sessao_idsessao']
        try:
            sessao = models.Sessao.objects.get(pk=ids.pk)
        except models.Sessao.DoesNotExist:
            raise ValidationError("Sessão não existe")
       
        if sessao.capacidade - sessao.nrinscritos  < cleaned_data['nr_inscritos']:
            raise ValidationError({'nr_inscritos': ["Não há vagas suficientes"]})
        
        #return True
    class Meta:
        model = models.InscricaoHasSessao
        fields = ['nr_inscritos','sessao_idsessao']
        widgets = {
            'sessao_idsessao': forms.NumberInput()
        }

###################################################END SESSOES#############################################
class CustomForm:
    def __init__(self,request = 0,**kwargs):
        self.curr_inscricao = None
        
        if 'inscricao' in kwargs and kwargs['inscricao'] != None:
            self.curr_inscricao = models.Inscricao.objects.get(pk=kwargs['inscricao'])

        Sessao = modelformset_factory(models.InscricaoHasSessao,form = Form_Sessao,extra=0,can_delete=True)
        Responsaveis = modelformset_factory(models.Responsaveis,form = Form_Responsaveis,min_num=1,extra=0,can_delete=True)
        Transportes = modelformset_factory(models.TransporteHasInscricao,form = Form_Transportes,extra=0,can_delete=True)


        if request != 0 and request.method == 'POST':
            if self.curr_inscricao != None:
                insc = models.InscricaoColetiva.objects.get(inscricao_idinscricao=self.curr_inscricao)
                self.escola = Form_Escola(request.POST,prefix="escola",instance=insc.escola_idescola)
                self.inscricao_coletiva = Form_InscricaoColetiva(request.POST,prefix="inscricao_coletiva",instance=insc)
                self.inscricao = Form_Inscricao(request.POST,prefix="inscricao",instance=self.curr_inscricao)
                self.responsaveis = Responsaveis(request.POST,prefix='responsaveis_set')
                self.sessao = Sessao(request.POST,prefix='sessao_set')
                self.transportes = Transportes(request.POST,prefix='transportes_set')
                self.almoco = Form_Almoco(request,instance=self.curr_inscricao)
            else:
                self.escola = Form_Escola(request.POST,prefix="escola")
                self.inscricao_coletiva = Form_InscricaoColetiva(request.POST,prefix="inscricao_coletiva")
                self.inscricao = Form_Inscricao(request.POST,prefix="inscricao")
                self.responsaveis = Responsaveis(request.POST,prefix='responsaveis_set')
                self.sessao = Sessao(request.POST,prefix='sessao_set')
                self.transportes = Transportes(request.POST,prefix='transportes_set')
                self.almoco = Form_Almoco(request)
        else:
            if self.curr_inscricao != None:
                insc = models.InscricaoColetiva.objects.get(inscricao_idinscricao=self.curr_inscricao)
                self.escola = Form_Escola(prefix="escola",instance=insc.escola_idescola)
                self.inscricao_coletiva = Form_InscricaoColetiva(prefix="inscricao_coletiva",instance=insc)
                self.inscricao = Form_Inscricao(prefix="inscricao",instance=self.curr_inscricao)
                self.responsaveis = Responsaveis(prefix='responsaveis_set',queryset=models.Responsaveis.objects.filter(idinscricao = self.curr_inscricao))
                self.sessao = Sessao(prefix='sessao_set',queryset=models.InscricaoHasSessao.objects.filter(inscricao_idinscricao = self.curr_inscricao))
                self.transportes = Transportes(prefix='transportes_set',queryset=models.TransporteHasInscricao.objects.filter(inscricao_idinscricao = self.curr_inscricao))
                self.almoco = Form_Almoco(request,instance=self.curr_inscricao)
            else:
                self.escola = Form_Escola(prefix="escola")
                self.inscricao_coletiva = Form_InscricaoColetiva(prefix="inscricao_coletiva")
                self.inscricao = Form_Inscricao(prefix="inscricao")
                self.responsaveis = Responsaveis(prefix='responsaveis_set',queryset=models.Responsaveis.objects.none())
                self.sessao = Sessao(prefix='sessao_set',queryset=models.InscricaoHasSessao.objects.none())
                self.transportes = Transportes(prefix='transportes_set',queryset=models.TransporteHasInscricao.objects.none())
                self.almoco = Form_Almoco(request)
        
    
    def is_valid(self):
        value = all([self.escola.is_valid(), self.inscricao.is_valid(), self.responsaveis.is_valid(), self.almoco.is_valid(),self.sessao.is_valid(),self.transportes.is_valid(),self.inscricao_coletiva.is_valid()])
        if len(self.sessao)<1:
            self.sessao.errors.append(SESSAO_MIN_ERROR)
            return False
        return value

    def save(self,part):
        escola = self.escola.save()
        inscricao = self.inscricao.save()
        self.inscricao_coletiva.save(part,escola,len(self.responsaveis),inscricao)
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
#   - inscricao_coletiva
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
