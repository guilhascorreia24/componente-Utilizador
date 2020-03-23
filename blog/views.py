
from django.shortcuts import render


def home(request):
    
    if 'user_id' in request.session :
        id=request.session['user_id']
        print(request.session.session_key)
    else:
        id=None
    return render(request, 'homepage.html', context={'id':id})
# Create your views here.
