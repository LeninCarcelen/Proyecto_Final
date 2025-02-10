from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import DVD
from .models import VHS
from .models import VideoEquipments
from catalogo.forms import DVDForm, VHSForm, VideoEquipmentsForm

def index(request):
    dvds = DVD.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(
        {
            'dvds':dvds,
        },
        request))

def VHSs(request):
    VHSs = VHS.objects.all()
    template = loader.get_template('client_list.html')
    return HttpResponse(template.render(
        {
            'vhss':VHSs,
        },
        request))

def Video_Equipments(request, VideoEquipments_id):
    videoEquipments = VideoEquipments.objects.get(id=VideoEquipments_id)
    template = loader.get_template('display_client.html')
    context = {
        'videoequipments': videoEquipments
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_DVD(request):
    if request.method == 'POST':
        form = DVDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm()
    
    return render(request, 'pokemon_form.html', {'form': form})

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

def delete_DVD(request, DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    dvd.delete()
    return redirect('catalogo:index')

def add_VHS(request):
    if request.method == 'POST':
        form = VHSForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm()
    
    return render(request, 'pokemon_form.html', {'form': form})

def edit_VHS(request, VHS_id):
    vhs = VHS.objects.get(id=VHS_id)
    if request.method == 'POST':
        form = VHSForm(request.POST, request.FILES, instance=vhs)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VHSForm(instance=vhs)
    
    return render(request, 'dvd_form.html', {'form': form})

def delete_VHS(request, VHS_id):
    vhs = VHS.objects.get(id=VHS_id)
    vhs.delete()
    return redirect('catalogo:index')

def add_VideoEquipments(request):
    if request.method == 'POST':
        form = VideoEquipmentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VideoEquipmentsForm()
    
    return render(request, 'pokemon_form.html', {'form': form})

def edit_VideoEquipments(request, VE_id):
    VideoEquipment = VideoEquipments.objects.get(id=VE_id)
    if request.method == 'POST':
        form = VideoEquipmentsForm(request.POST, request.FILES, instance=VideoEquipment)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VideoEquipmentsForm(instance=VideoEquipment)
    
    return render(request, 'dvd_form.html', {'form': form})

def delete_VideoEquipments(request, VE_id):
    VideoEquipment = VideoEquipments.objects.get(id=VE_id)
    VideoEquipment.delete()
    return redirect('catalogo:index')

class CustomLoginView(LoginView):
    template_name = "login_form.html"