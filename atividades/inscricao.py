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
