from django.shortcuts import render, get_object_or_404, redirect, reverse
import datetime, time
from .forms import *
from .models import *
from .filters import *
from Notification.views import noti_not_checked
from user.views import update_ano_user_null

###### Dia Aberto ##############
def index(request):
    queryset = DiaAberto.objects.all() # list of objects
    context = {
        "diaaberto": queryset,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "index.html", context)
'''def preencher_hora(hora_incio, hora_fim):
    inter=datetime.time(0,30,0)
    while inter<hora_fim:
        Horario.objects.create(pk=hora_inicio)
        hora_incio+=inter
    Horario.objects.create(pk=hora_fim)'''

def diaaberto_create(request):
    user = Utilizador.objects.get(idutilizador=request.session['user_id'])
    admin = Administrador.objects.get(utilizador_idutilizador=user)
    new_form = DiaAberto(administrador_utilizador_idutilizador=admin)
    form = DiaAbertoForm(request.POST or None, instance=new_form)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            inicio = form.cleaned_data['datadiaabertoinicio']
            final = form.cleaned_data['datadiaabertofim']
            #preencher_hora(hora_inicio,hora_fim)
            Horario(hora="12:00:00").save()
            hora1 = Horario.objects.filter(hora="12:00:00")
            for x in range(inicio.day, final.day):
                Dia(dia=inicio+datetime.timedelta(days=x)).save()
                dia1 = Dia.objects.filter(dia = inicio+datetime.timedelta(days=x))
                HorarioHasDia(horario_hora=hora1[0], dia_dia=dia1[0]).save()
            update_ano_user_null()
            return redirect("blog:blog-home")
    return render(request,
                 template_name="DiaAberto/diaaberto_create.html", 
                    context={'form': form,'o':True,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})


def diaaberto_update(request, id):
    
    obj = get_object_or_404(DiaAberto, ano=id)
    form = DiaAbertoForm(request.POST or None, instance=obj)
    pk_url_kwarg = 'ano'
    if form.is_valid():
        form.save()
        return redirect("blog:blog-home")
    context = {
        'form': form,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "DiaAberto/diaaberto_create.html", context)


def diaaberto_list(request):
    d = DiaAberto.objects.all() # list of objects
    dia = DiaAberto.objects.order_by('-ano')
    myFilter = DiaAbertoFilter(request.GET, queryset=dia)
    dia = myFilter.qs
    context = {
        "diaaberto_list": dia,
        'myFilter': myFilter,
        "d": d,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "DiaAberto/diaaberto_list.html", context)

def diaaberto_details(request, id):
    obj = get_object_or_404(DiaAberto, ano=id)
    pk_url_kwarg = 'ano'
    context = {
        "diaaberto": obj,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "DiaAberto/diaaberto_details.html", context)


def diaaberto_delete(request, id):
    obj = get_object_or_404(DiaAberto, ano=id)
    if DiaAberto.objects.filter(ano=id).exists():
        obj.delete()
    return redirect('menu:diaaberto_list')

### Menuuuu ###########
def menu_create_view(request):
    form = MenuModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("menu:menu_list")
    context = {
        'form': form,'o':True,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Menu/menu_create.html", context)


def prato_create_view(request):
    form = PratoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("menu:menu_list")
    context = {
        'form': form,'o':True,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
                  }
    return render(request, "Menu/prato_create.html", context)

def menu_update_view(request, id):
    obj = get_object_or_404(Menu, idmenu=id)
    form = MenuModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("menu:menu_list")
    context = {
        'form': form,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Menu/menu_create.html", context)

def prato_update_view(request, id):
    obj = get_object_or_404(Prato, idprato=id)
    form = PratoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("menu: ")
    context = {
        'form': form,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Menu/prato_create.html", context)


def menu_list_view(request):
    menu = Menu.objects.all() # list of objects
    campus= Campus.objects.all()
    prato=Prato.objects.all()
    preco=DiaAberto.objects.all()
    atual=datetime.date.today().year
    context = {
        "menu": menu,
        "campus": campus,
        "prato":prato,'preco':preco,'atual':atual,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)

    }
    return render(request, "Menu/menu_list.html", context)



def menu_detail_view(request, id):
    obj = get_object_or_404(Menu, idmenu=id)
    prato = Prato.objects.filter(menu_idmenu=id)
    preco = DiaAberto.objects.all()
    context = {
        "menu": obj,
        "prato": prato,
        "preco": preco,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Menu/menu_details.html", context=context)


def menu_delete_view(request, id):
    obj = get_object_or_404(Menu, idmenu=id)
    if Menu.objects.filter(pk=id).exists():
        obj.delete()
    return redirect('menu:menu_list')

def prato_delete_view(request, id):
    obj = get_object_or_404(Prato, idprato=id)
    if Prato.objects.filter(pk=id).exists():
        obj.delete()
    return redirect('blog:blog-home')

######## TRANSPORTEEE ############################
def transporte_create_view(request):
    form = TransportForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("menu:horario-list")
    context = {
        'form': form,'o':True,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Transporte/transporte_create.html", context)

def horario_create_view(request):
    hora = HorarioHasDia.objects.all()
    utl = Transporte.objects.latest('idtransporte')
    new_form = TransporteHasHorario(transporte_idtransporte = utl, n_passageiros= 0)
    form = TransporteHorarioForm(request.POST, instance = new_form)
    if request.method == "POST":
        if form.is_valid():
            new_horario = form.save(commit=False)
            org = Paragem.objects.get(paragem = request.POST['origem'])
            dest = Paragem.objects.get(paragem = request.POST['destino'])
            hor = HorarioHasDia.objects.get(id_dia_hora = request.POST['horario_has_dia_id_dia_hora'])
            new_horario.origem = org
            new_horario.destino = dest
            new_horario.horario_has_dia_id_dia_hora = hor
            new_horario.save()
            return redirect("menu:transporte-list")
    context = {
        'form': form,
        'hora' : hora,'o':True,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Transporte/horario_create.html", context)


def transporte_update_view(request, id):
    form1 = get_object_or_404(TransporteHasHorario, id_transporte_has_horario=id)
    obj = get_object_or_404(Transporte, idtransporte=form1.transporte_idtransporte.pk) 
    form = TransportForm(request.POST or None, instance=obj)
    print("uuuuuuuuuuuuuuuuuuuuu")
    if form.is_valid():
        form.save()
        return redirect('menu:transporte-update2', id=id)
    context = {
        'form': form,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Transporte/transporte_create.html", context)

def transporte_update2_view(request, id):
    obj = get_object_or_404(TransporteHasHorario, id_transporte_has_horario=id)
    hora = HorarioHasDia.objects.all()
    print(obj)
    form = TransporteHorarioForm(request.POST or None, instance=obj)
    if form.is_valid():
        print("aaaaaaaaaaaaaaaaaaaa")
        form.save()
        return redirect("/transporte")
    context = {
        'form': form,
        'hora': hora,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    print(form.errors)
    return render(request, "Transporte/horario_create.html", context)


def transporte_list_view(request):
    hora = TransporteHasHorario.objects.all()
    par = Paragem.objects.all()

    context = {
        "hora": hora,
        "par": par,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Transporte/transporte_list.html", context)

def transporte_detail_view(request, id):
    obj = get_object_or_404(Transporte,idtransporte =id)
    transporte = TransporteHasHorario.objects.get(transporte_idtransporte=id)
    context = {
        "obj": obj,
        "transporte": transporte,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)

    }
    return render(request, "Transporte/transporte_details.html", context)


def transporte_delete_view(request, id):
	transporte = Transporte.objects.get(idtransporte=id)
	if Transporte.objects.filter(pk=id).exists():
		transporte.delete()
	return redirect("menu:transporte-list")

def transportehora_create_view(request):
    form1 = DiaForm(request.POST or None)
    form2 = HoraForm(request.POST or None)
    if request.method == "POST":
        if form1.is_valid() & form2.is_valid():
            form1.save()
            form2.save()
            utl = Horario.objects.latest('hora')
            utl1 = Dia.objects.latest('dia')
            horario = HorarioHasDia(horario_hora=utl, dia_dia=utl1)
            horario.save()
            return redirect("menu:transporte-list")
    context = {
        'form1': form1,
        'form2': form2,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Transporte/hora_create.html", context)
