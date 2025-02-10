from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import DVD
from .models import VHS
from .models import VideoEquipments
from catalogo.forms import DVDForm, VHSForm, VideoEquipmentsForm

#Catalogo inicio

def index(request):
    dvds = DVD.objects.all()
    vhss = VHS.objects.all()
    video_equipments = VideoEquipments.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(
        {
            'dvds': dvds,
            'vhss': vhss,
            'videoequipments': video_equipments,
        },
        request))

#Listas

def DVDs(request):
    dvds = DVD.objects.all()
    template = loader.get_template('dvd_list.html')
    return HttpResponse(template.render(
        {
            'dvds':dvds,
        },
        request))

def VHSs(request):
    VHSs = VHS.objects.all()
    template = loader.get_template('vhs_list.html')
    return HttpResponse(template.render(
        {
            'vhss':VHSs,
        },
        request))

def Video_Equipments(request, VideoEquipments_id):
    videoEquipments = VideoEquipments.objects.get(id=VideoEquipments_id)
    template = loader.get_template('video_equipments_list.html')
    context = {
        'videoequipments': videoEquipments
    }
    return HttpResponse(template.render(context, request))

#Información (Display)

def dvd(request, DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    template = loader.get_template('display_dvd.html')
    context = {
        'dvd': dvd
    }
    return HttpResponse(template.render(context, request))

def vhs(request, VHS_id):
    vhs = VHS.objects.get(id=VHS_id)
    template = loader.get_template('display_vhs.html')
    context = {
        'vhs': vhs
    }
    return HttpResponse(template.render(context, request))

def video_equipment(request, VE_id):
    videoEquipments = VHS.objects.get(id=VE_id)
    template = loader.get_template('display_video_equipments.html')
    context = {
        'videoEquipments': videoEquipments
    }
    return HttpResponse(template.render(context, request))

@login_required

# DVD VIEWS

def add_DVD(request):
    if request.method == 'POST':
        form = DVDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm()
    
    return render(request, 'dvd_form.html', {'form': form})

def edit_DVD(request, DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    if request.method == 'POST':
        form = DVDForm(request.POST, request.FILES, instance=dvd)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm(instance=dvd)
    
    return render(request, 'dvd_form.html', {'form': form})

def delete_DVD(DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    dvd.delete()
    return redirect('catalogo:index')

# VHS VIEWS

def add_VHS(request):
    if request.method == 'POST':
        form = VHSForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm()
    
    return render(request, 'vhs_form.html', {'form': form})

def edit_VHS(request, VHS_id):
    vhs = VHS.objects.get(id=VHS_id)
    if request.method == 'POST':
        form = VHSForm(request.POST, request.FILES, instance=vhs)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VHSForm(instance=vhs)
    
    return render(request, 'vhs_form.html', {'form': form})

def delete_VHS(VHS_id):
    vhs = VHS.objects.get(id=VHS_id)
    vhs.delete()
    return redirect('catalogo:index')

# VIDEO_EQUIPMENTS VIEWS

def add_VideoEquipments(request):
    if request.method == 'POST':
        form = VideoEquipmentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VideoEquipmentsForm()
    
    return render(request, 'video_equipments_form.html', {'form': form})

def edit_VideoEquipments(request, VE_id):
    VideoEquipment = VideoEquipments.objects.get(id=VE_id)
    if request.method == 'POST':
        form = VideoEquipmentsForm(request.POST, request.FILES, instance=VideoEquipment)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VideoEquipmentsForm(instance=VideoEquipment)
    
    return render(request, 'video_equipments_form', {'form': form})

def delete_VideoEquipments(VE_id):
    VideoEquipment = VideoEquipments.objects.get(id=VE_id)
    VideoEquipment.delete()
    return redirect('catalogo:index')

class CustomLoginView(LoginView):
    template_name = "login_form.html"