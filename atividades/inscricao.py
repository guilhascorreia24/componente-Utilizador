from atividades import forms
from django.shortcuts import render, redirect, HttpResponse

def show(request):
    if request.method == 'POST':
        form = forms.CustomForm(request)
        if form.is_valid():
            form.save()
            return HttpResponse("<html>Sucess</html>")
        
        
    else:
        form = forms.CustomForm()
        return render(request,'test.html',{'form': form})

def showForm(request):
    inscricao = forms.Form_Inscricao()
    responsaveis = forms.Form_Responsaveis()
    escola = forms.Form_Escola()
    insColetiva = forms.Form_InscricaoColetiva()

    if request.method == 'POST':
        print("Saving\n")
        (escolaTest,escola) = saveEscola(request)
        if escolaTest == False:
            print("Leaving")
            return render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})

        print("Saving1\n")
        (insTest,inscricao) = saveInscricao(request)
        if insTest == False:
            return render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})

        #(insColetivaTest,insColetiva) = saveInscricaoColetiva(request)
        #if insColetivaTest == False:
        #    return render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})

        (respTest,numResponsaveis) = saveResponsavel(request,inscricao.idinscricao)
        if respTest == False:
            render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})
    
    return render(request,'atividades_participante_show.html',{'inscricao': inscricao,'responsaveis':responsaveis, 'escola':escola , 'insColetiva' : insColetiva})



def saveResponsavel(request,idInscricao):
    form = forms.Form_Responsaveis(request.POST,prefix="a")
    if form.is_valid():
        result = form.save(idInscricao)
        return (True,result)

    return (False,form)

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
    escola_form = forms.Form_Escola(request.POST,prefix = "b")
    if escola_form.is_valid():
        result = escola_form.save()
        return (True,result)

    print(escola_form)
    return (False,escola_form)


def saveInscricaoColetiva(request,idUtilizador,idInscricao,idEscola):
    form = forms.Form_InscricaoColetiva(request.POST)
    if form.is_valid():
        result = form.save(idUtilizador,idInscricao,idEscola)
        return (True,result)

    return (False,form)

def saveInscricao(request):
    form = forms.Form_Inscricao(request.POST,prefix = "c")
    if form.is_valid():
        result = form.save()
        return (True,result)

    return (False,form)