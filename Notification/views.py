from django.shortcuts import render
from Notification import templates
from .models import Notificacao
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def createnot(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("<h2>Sent sucessfully</h2>")
	else:
		form = UserRegisterForm()

	return render(request,'notification.html',{'form':form})

def checknot(request):
	id=request.session['user_id']

	return render(request,'check.html')