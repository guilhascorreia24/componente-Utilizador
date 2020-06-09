from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory,ValidationError
from django import forms
from inscricao import models
from inscricao.validators import email_validator, not_zero_validator, telefone_validator, SESSAO_MIN_ERROR
from django.db.models import F
from inscricao import validators

class Form_Responsaveis(ModelForm):

    def set_inscricao(self,inscricao):
        self._idinscricao = inscricao
    def save(self,**kwargs):
        idinscricao = self._idinscricao
        base = super(Form_Responsaveis, self).save(commit=False)
        base.idinscricao = idinscricao
        base.save()
        return base

    class Meta:
        model = models.Responsaveis
        fields = ['nome','email','telefone']

class Form_InscricaoColetiva(ModelForm):
    def save(self, idUtilizador, idEscola, nresponsaveis, inscricao, local):
        base = super(Form_InscricaoColetiva, self).save(commit=False)
        base.local = local
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

    def save(self,local):
        base = super(Form_Inscricao, self).save(commit=False)
        base.local = local
        base.save()
        return base

class Form_Escola(ModelForm):

    class Meta:
        model = models.Escola
        fields = ['nome','local','telefone','email']

###################### TRANSPORTES ########################################

#Check if is full
class Form_Transportes(ModelForm):

    def __init__(self, **kwargs):
        super(Form_Transportes, self).__init__(**kwargs)
        #Ignore full transportes NEEDS CHECK
        self.fields['horario'].queryset = models.TransporteHasHorario.objects.annotate(ratio=F('transporte_idtransporte__capacidade')-F('n_passageiros')).filter(ratio__gt=0)

    def set_inscricao(self,inscricao):
        self._idinscricao = inscricao
        
    def save(self,**kwargs):
        idinscricao = self._idinscricao
        base = super(Form_Transportes, self).save(commit=False)
        base.inscricao_idinscricao = idinscricao
        base.save()
        return base

    class Meta:
        model = models.TransporteHasInscricao
        fields = ['horario','n_passageiros']


########################Almoços###########################


class Form_Almoco:
    def __init__(self, request=0,**kwargs):
        if 'instance' in kwargs:
            self.curr_insc = kwargs['instance']
        else:
            self.curr_insc = None

        campus = models.Campus.objects.all()
        menus = list()
        self.prato = list()
        for camp in campus:
            queryset = models.Menu.objects.filter(campus_idcampus = camp)
            for query in queryset:
                menus.append(query)

        #New BD entry
        if(self.curr_insc == None):
            if request != 0 and request.method == 'POST':
                for menu in menus:
                    self.prato.append(Form_Prato(request.POST,menu=menu,prefix='menu_'+str(menu.pk)))
            else:
                for menu in menus:
                    self.prato.append(Form_Prato(menu=menu,prefix='menu_'+str(menu.pk)))
        
        #Change BD Entry
        else:
            instances = models.InscricaoHasPrato.objects.select_related('prato_idprato').filter(inscricao_idinscricao = self.curr_insc)
            self.instances_dict = dict()
            for instance in instances:
                self.instances_dict[instance.prato_idprato.menu_idmenu.pk] = instance.prato_idprato
                print(instance.prato_idprato.menu_idmenu.pk)
            if request != 0 and request.method == 'POST':
                for menu in menus:
                    if menu.pk in self.instances_dict:
                        self.prato.append(Form_Prato(request.POST,menu=menu,instance=self.instances_dict[menu.pk],prefix='menu_'+str(menu.pk)))
                    else:
                        self.prato.append(Form_Prato(request.POST,menu=menu,prefix='menu_'+str(menu.pk)))
            else:
                for menu in menus:
                    if menu.pk in self.instances_dict:
                        self.prato.append(Form_Prato(menu=menu,instance=self.instances_dict[menu.pk],prefix='menu_'+str(menu.pk)))
                    else:
                        self.prato.append(Form_Prato(menu=menu,prefix='menu_'+str(menu.pk)))

    #Check 0 values while other errors occurr
    def is_valid(self):
        value = True
        for prato in self.prato:
            if not prato.is_valid():
                value = False
        
        return value

#If prato already exists and new one has 0 almocos, delete the older one
#If has 0 almocos and doesn't exist skip it
#If isn't zero, add it or update-it
    def save(self,inscricao):
        if self.curr_insc != None:
            for prato in self.prato:
                nr = prato.cleaned_data['nralmocos']
                if(nr == 0):
                    if prato.menu.pk in self.instances_dict:
                        self.instances_dict[prato.menu.pk].delete()
                    else:
                        continue
                else:
                    if prato.menu.pk in self.instances_dict:
                        prato.save()
                    else:
                        prato_result = prato.save()
                        models.InscricaoHasPrato(inscricao_idinscricao=inscricao,prato_idprato=prato_result).save()

        else:
            for prato in self.prato:
                if(prato.cleaned_data['nralmocos'] == 0):
                    continue
                else:
                    prato_result = prato.save()
                    models.InscricaoHasPrato(inscricao_idinscricao=inscricao,prato_idprato=prato_result).save()


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
        if self.instance.pk != None:
            almocos = self.menu.nralmocosdisponiveis - self.instance.nralmocos
        else:
            almocos = self.menu.nralmocosdisponiveis
        if almocos < self.cleaned_data['nralmocos']:
            msg = validators.ALMOCOS_FULL.replace('_NUM_',str(self.menu.nralmocosdisponiveis))
            raise ValidationError({'nralmocos': msg})

    class Meta:
        model = models.Prato
        fields = ['nralmocos']


###################################################END ALMOÇO #########################################

###################################################SESSOES#############################################

class Form_Sessao(ModelForm):
    #sessao_id = forms.IntegerField()

    def set_inscricao(self,inscricao):
        self._idinscricao = inscricao

    def save(self,**kwargs):
        inscricao = self._idinscricao
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


        valid_nr = sessao.capacidade - sessao.nrinscritos
        if self.instance.pk != None:
            valid_nr += self.instance.nr_inscritos


       
        if valid_nr  < cleaned_data['nr_inscritos']:
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
        print(Responsaveis)
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
                self.almoco = Form_Almoco(instance=self.curr_inscricao)
            else:
                self.escola = Form_Escola(prefix="escola")
                self.inscricao_coletiva = Form_InscricaoColetiva(prefix="inscricao_coletiva")
                self.inscricao = Form_Inscricao(prefix="inscricao")
                self.responsaveis = Responsaveis(prefix='responsaveis_set',queryset=models.Responsaveis.objects.none())
                self.sessao = Sessao(prefix='sessao_set',queryset=models.InscricaoHasSessao.objects.none())
                self.transportes = Transportes(prefix='transportes_set',queryset=models.TransporteHasInscricao.objects.none())
                self.almoco = Form_Almoco()
        
    
    def is_valid(self):
        value = all([self.escola.is_valid(), self.inscricao.is_valid(), self.responsaveis.is_valid(), self.almoco.is_valid(),self.sessao.is_valid(),self.transportes.is_valid(),self.inscricao_coletiva.is_valid()])
        if len(self.sessao)<1:
            self.sessao.errors.append(SESSAO_MIN_ERROR)
            return False
        return value

    def save(self,part):
        escola = self.escola.save()
        inscricao = self.inscricao.save(escola.local)
        self.inscricao_coletiva.save(part,escola,len(self.responsaveis),inscricao,escola.local)
        self.almoco.save(inscricao)

        for each in self.transportes:
            each.set_inscricao(inscricao)


        for each in self.sessao:
            each.set_inscricao(inscricao)
        
        
        for each in self.responsaveis:
            each.set_inscricao(inscricao)
        
        self.responsaveis.save()
        self.transportes.save()
        self.sessao.save()

        #Delete

        return self


#TEMPLATE

# - form
#   - inscricao
#   - inscricao_coletiva
#   - escola
#   - sessao
#   - responsaveis
#   - almoco
#           - prato (array)
#               - menu
#               - nralmocos
#   - transportes
#       -campus (array)
#           - nome  (nome do campus)
#           - transporte
