from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path("", views.index, name="index"),
    path("VHSs/", views.VHSs, name="VHSs"),
    path("Video_Equipments/<int:VideoEquipments_id>/", views.Video_Equipments, name="Video_Equipments"),
    path("add_DVD/", views.add_DVD, name="add_DVD"),
    path("edit_DVD/<int:DVD_id>", views.edit_DVD, name="edit_DVD"),
    path("delete_DVD/<int:DVD_id>", views.delete_DVD, name="delete_DVD"),
    path("add_VHS/", views.add_VHS, name="add_VHS"),
    path("edit_VHS/<int:VHS_id>", views.edit_VHS, name="edit_VHS"),
    path("delete_VHS/<int:VHS_id>", views.delete_VHS, name="delete_VHS"),
    path("add_VideoEquipments/", views.add_VideoEquipments, name="add_VideoEquipments"),
    path("edit_VideoEquipments/<int:VE_id>", views.edit_VideoEquipments, name="edit_VideoEquipments"),
    path("delete_VideoEquipments/<int:VE_id>", views.delete_VideoEquipments, name="delete_VideoEquipments"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]