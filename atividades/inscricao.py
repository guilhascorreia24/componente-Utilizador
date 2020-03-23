from atividades import forms
from django.shortcuts import render, redirect


def showForm(request):
    inscricao = forms.Form_Inscricao()
    responsaveis = forms.Form_Responsaveis()
    escola = forms.Form_Escola()
    insColetiva = forms.Form_InscricaoColetiva()

    if request.method == 'POST':
        (insTest,inscricao) = saveInscricao(request)
        if insTest == False:
            return render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})

        (escolaTest,escola) = saveEscola(request)
        if escolaTest == False:
            return render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})

        (insColetivaTest,insColetiva) = saveInscricaoColetiva(request)
        if insColetivaTest == False:
            return render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})

        (respTest,numResponsaveis) = saveResponsavel(request,inscricao.idinscricao)
        if respTest == False:
            render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})
    
    return render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})



def saveResponsavel(request,idInscricao):
    form = forms.Form_Responsaveis
    if form.is_valid():
        form.fill(idInscricao)
        result = form.save()
        return (True,result)

    return (False,escola_form)

#If true return number of reponsaveis existent
def saveResponsaveis(request,idinscricao):
    resp = formset_factory(forms.Form_Responsaveis)
    resp_set = resp(request.POST)
    if resp_set.is_valid():
        counter = 0
        for _form in resp_set:
            _form.fill(idinscricao)
            _form.save()
            counter += 1
        return (True,counter)

    return (False,resp_set)


def saveEscola(request):
    esola_form = forms.Form_Escola(request.POST)
    if escola_form.is_valid():
        result = escola_form.save()
        return (True,result)

    return (False,escola_form)


def saveInscricaoColetiva(request,idUtilizador,idInscricao,idEscola):
    form = forms.InscricaoColetiva(request.POST)
    if form.is_valid():
        form.fill(idUtilizador,idInscricao,idEscola)
        result = form.save()
        return (True,result)

    return (False,escola_form)

def saveInscricao(request):
    form = forms.Inscricao(request.POST)
    if form.is_valid():
        form.save()
        return (True,0)

    return (False,escola_form)