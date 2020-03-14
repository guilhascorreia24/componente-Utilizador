
from django.shortcuts import render


def home(request):
    #id=request.session['id']
    return render(request, 'homepage.html', context={})
# Create your views here.
