from django.shortcuts import render, get_object_or_404, redirect, reverse
import datetime, time
from django.contrib import messages
from .forms import *
from .models import *
from Notification.views import noti_not_checked
from user.views import update_ano_user_null
from django.utils import timezone
from django.contrib import messages
from Notification import views as noti_views
from django.db.models import CharField, Value, TimeField
###### Dia Aberto ##############
def index(request):
    queryset = DiaAberto.objects.all() # list of objects
    context = {
        "diaaberto": queryset,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "index.html", context)

def preencher_hora(hora_incio, hora_fim):
    time_start = datetime.datetime.strptime(hora_incio, '%H:%M')
    time_end = datetime.datetime.strptime(hora_fim, '%H:%M')

    while time_start < time_end:
        time_start += datetime.timedelta(minutes=30)
        Horario.objects.get_or_create(pk=time_start)
    return Horario.objects.all()


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
            hora_inicio=request.POST['h_incio']
            hora_fim=request.POST['h_fim']
            hora_list = preencher_hora(hora_inicio,hora_fim)
            Horario(hora="09:00:00").save()
            Horario(hora="08:30:00").save()
            for x in range(inicio.day, final.day+1):
                Dia(dia=inicio+datetime.timedelta(days=x-inicio.day)).save()
                dia1 = Dia.objects.filter(dia = inicio+datetime.timedelta(days=x-inicio.day))
                for hora in hora_list:
                    if HorarioHasDia.objects.filter(horario_hora=hora, dia_dia=dia1[0]).exists():
                        continue
                    HorarioHasDia(horario_hora=hora, dia_dia=dia1[0]).save()
            update_ano_user_null()
            messages.success(request, f'Dia Aberto Criado com Sucesso!')
            return redirect("menu:diaaberto_list")
    return render(request,
                 template_name="DiaAberto/diaaberto_create.html", 
                    context={'form': form,'o':True,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})


def diaaberto_update(request, id):
    
    obj = get_object_or_404(DiaAberto, ano=id)
    form = DiaAbertoForm(request.POST or None, instance=obj)
    pk_url_kwarg = 'ano'
    hora_inicio=Horario.objects.all()[0].pk
    hora_fim=Horario.objects.all().order_by('-pk')[0].pk
    print(hora_inicio)
    horarios=HorarioHasDia.objects.all()
    for horario in horarios:
        if horario.dia_dia.pk.year==id:
            if horario.horario_hora.pk<hora_inicio:
                hora_inicio=HorarioHasDia.objects.filter(dia_dia=horario.dia_dia)[0].horario_hora.pk
            if horario.horario_hora.pk>hora_fim:
                hora_fim=HorarioHasDia.objects.filter(dia_dia=horario.dia_dia).reverse()[0].horario_hora.pk
    if form.is_valid():
        form.save()
        #Horario.objects.all().delete()
        inicio = form.cleaned_data['datadiaabertoinicio']
        final = form.cleaned_data['datadiaabertofim']
        #preencher_hora(hora_inicio,hora_fim)
        print(request.POST)
        hora_inicio=request.POST['h_incio']
        hora_fim=request.POST['h_fim']
        hora_list = preencher_hora(hora_inicio,hora_fim)
        Horario(hora="09:00:00").save()
        Horario(hora="08:30:00").save()
        for x in range(inicio.day, final.day+1):
            Dia(dia=inicio+datetime.timedelta(days=x-inicio.day)).save()
            dia1 = Dia.objects.filter(dia = inicio+datetime.timedelta(days=x-inicio.day))
            for hora in hora_list:
                if HorarioHasDia.objects.filter(horario_hora=hora, dia_dia=dia1[0]).exists():
                    continue
                HorarioHasDia(horario_hora=hora, dia_dia=dia1[0]).save()
        messages.success(request, f'Dia Aberto editado com Sucesso!')
        return redirect("menu:diaaberto_list")
    context = {
        'form': form,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "DiaAberto/diaaberto_create.html", context)


def diaaberto_list(request):
    d = DiaAberto.objects.all() # list of objects
    dia = DiaAberto.objects.order_by('-ano').annotate(hora_inicio=Value(datetime.time(23,59),TimeField()),hora_fim=Value(datetime.time(23,59),TimeField()))
    hora_inicio=Horario.objects.all()[0]
    hora_fim=Horario.objects.all().order_by('-pk')[0]
    horarios=HorarioHasDia.objects.all()
    for de in dia:
        de.hora_inicio=Horario.objects.all()[0].pk
        de.hora_fim=Horario.objects.all().order_by('-pk')[0].pk
        for horario in horarios:
            if horario.dia_dia.pk.year==de.ano:
                if horario.horario_hora.pk<de.hora_inicio:
                    de.hora_inicio=HorarioHasDia.objects.filter(dia_dia=horario.dia_dia)[0].horario_hora.pk
                if horario.horario_hora.pk>de.hora_fim:
                    de.hora_fim=HorarioHasDia.objects.filter(dia_dia=horario.dia_dia).reverse()[0].horario_hora.pk
    context = {
        "diaaberto_list": dia,
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
        user=request.session['user_id']
        if Utilizador.objects.filter(dia_aberto_ano=id,pk=request.session['user_id']).exists():
            del request.session['user_id']
            del request.session['type']
        obj.delete()
        if not(Utilizador.objects.filter(pk=user).exists()):
            notis=Notificacao.objects.all()
            dias=Dia.objects.all()
            for noti in notis:
                if noti.criadoem.year==id:
                    noti.delete()
            for dia in dias:
                if dia.pk.year==id:
                    dia.delete()
            return redirect("blog:blog-home")
        messages.success(request, f'Configurações do Dia Aberto eliminado com Sucesso!')
        noti_views.new_noti(request,request.session['user_id'],'Submissao das Configurações do Dia Aberto','Configurações do Dia Aberto eliminado com Sucesso!')
    return redirect('menu:diaaberto_list')

### Menuuuu ###########
def menu_create_view(request):
    form = MenuModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Menu Criado com Sucesso!')
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
        messages.success(request, f'Prato Criado com Sucesso!')
        return redirect("menu:menu_list")
    context = {
        'form': form,'o':True,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
                  }
    return render(request, "Menu/prato_create.html", context)

def menu_update_view(request, id):
    obj = get_object_or_404(Menu, idmenu=id)
    form = MenuModelForm(request.POST or None, instance=obj)
    pk_url_kwarg = 'idmenu'
    if form.is_valid():
        form.save()
        messages.success(request, f'Menu Editado com Sucesso!')
        return redirect("menu:menu_list")
    context = {
        'form': form,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Menu/menu_create.html", context)

def prato_update_view(request, id):
    obj = get_object_or_404(Prato, idprato=id)
    form = PratoForm(request.POST or None, instance=obj)
    pk_url_kwarg = 'idprato'
    if form.is_valid():
        form.save()
        messages.success(request, f'Prato Editado com Sucesso!')
        return redirect("menu:menu_list")
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
        Prato.objects.filter(menu_idmenu=Menu.objects.get(pk=id)).delete()
        Menu.objects.filter(pk=id).delete()
        messages.success(request, f'Menu Eliminado com Sucesso!')
    return redirect('menu:menu_list')

def prato_delete_view(request, id):
    obj = get_object_or_404(Prato, idprato=id)
    if Prato.objects.filter(pk=id).exists():
        obj.delete()
        messages.success(request, f'Prato Eliminado com Sucesso!')
    return redirect('menu:menu_list')

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
            messages.success(request, f'Transporte Criado com Sucesso!')
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
        messages.success(request, f'Transporte Editado com Sucesso!')
        return redirect("menu:transporte-list")
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
    inscricao = TransporteHasInscricao.objects.get(inscricao_idinscricao=id)
    context = {
        "obj": obj,
        "transporte": transporte,
        "inscricao": incricao,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)

    }
    return render(request, "Transporte/transporte_details.html", context)

def transporte_delete_view(request,id):
    transporte = Transporte.objects.get(idtransporte=id)
    if Transporte.objects.filter(pk=id).exists():
        transporte.delete()
        messages.success(request, f'Transporte Eliminado com Sucesso!')
    return redirect("menu:transporte-list")

def transportehora_create_view(request):
    form = HoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Horário Criado com Sucesso!')
        return redirect("menu:transporte-list")
    context = {
        'form': form,'o':True,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Transporte/hora_create.html", context)



def horariotransporte_create_view(request):
    form = HorarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Horário do Transporte Criado com Sucesso')
        return redirect("menu:transporte-list")
    context = {
        'form': form,'o':True,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Transporte/horariotrans_create.html", context)


def transporte_grupo_view(request, id):
    form = InscricaoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(id)
            print("aaaaaaaaaaaaaaaaaaa")
            messages.success(request, f'Transporte associado com Sucesso!')
            noti_views.new_noti(request,request.session['user_id'],'Submissao do Transporte','  Transporte Associado com Sucesso!')
            return redirect("menu:transporte-list")
            
    context = {
        'form': form,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "Transporte/grupos_ass.html", context)


