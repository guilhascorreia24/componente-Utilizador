from django.shortcuts import render, redirect, HttpResponse
from inscricao import models
from django.contrib.auth import authenticate, login, logout
from blog import userValidation
from inscricao import forms
from django.forms import formset_factory

# Main Views.
def test(request):
    #return inscricao.showForm(request)
    form = forms.Form_Escola()
    return render(request,'test2.html',{'form': form})

def test1(request):
    if request.method == 'POST':
        form = forms.CustomForm(request)
        if form.is_valid():
            form.save()
            return HttpResponse("<html>Sucess</html>")
        else:
            return render(request,'test.html',{'form': form})
        
    else:
        form = forms.CustomForm()
        return render(request,'test.html',{'form': form})


def inscricao_form(request):
    form = forms.CustomForm(request)
    return render(request,'inscricao_form.html',{'form' : form})