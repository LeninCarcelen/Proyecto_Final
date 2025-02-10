from django import forms
from .models import DVD
from .models import VHS
from .models import VideoEquipments

class DVDForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'year': 'año',
            'genre': 'Género',
            'description': 'Descripción',
            'price': 'Precio',
            'picture': 'Foto',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class VHSForm(forms.ModelForm):
    class Meta:
        model = VHS
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'year': 'año',
            'type': 'Tipo',
            'description': 'Descripción',
            'price': 'Precio',
            'picture': 'Foto',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class VideoEquipmentsForm(forms.ModelForm):
    class Meta:
        model = VideoEquipments
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'year': 'año',
            'genre': 'Género',
            'description': 'Descripción',
            'price': 'Precio',
            'picture': 'Foto',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }