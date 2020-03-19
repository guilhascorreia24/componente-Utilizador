
from django.shortcuts import render


def home(request):
    if request.session['user_id']:
        id=request.session['user_id']
    else:
        id=None
    return render(request, 'homepage.html', context={'id':id})
# Create your views here.
