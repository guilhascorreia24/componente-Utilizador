
from django.shortcuts import render


def home(request):
    if 'cookie_id' in request.COOKIES:
        print("cookie:"+request.COOKIES['cookie_id'])
        request.session['user_id']=request.COOKIES['cookie_id']
    if 'user_id' in request.session:
        print("session:"+str(request.session['user_id']))
        id=request.session['user_id']
    else:
        id=None
    return render(request, 'homepage.html', context={'id':id})
# Create your views here.
