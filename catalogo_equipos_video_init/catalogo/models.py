from django.db import models

class DVD(models.Model):
    title = models.CharField(max_length=30, null=False)
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)
    GENRE_TYPES = {
        ('AC', 'Acción'),
        ('AV', 'Aventura'),
        ('T', 'Terror'),
        ('CF', 'Ciencia ficción'),
        ('C', 'Comedia'),
        ('D', 'Drama'),
    }
    genre = models.CharField(max_length=30, choices=GENRE_TYPES, null=False)
    description = models.CharField(max_length=300, null=False)
    price = models.DecimalField(decimal_places=4, max_digits=6)
    picture = models.ImageField(upload_to="catalogo_images")
    
    def __str__(self):
        return self.title

class VHS(models.Model):
    title = models.CharField(max_length=30, null=False)
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)
    VHS_TYPE = {
        ('P', 'Película'),
        ('M', 'Música'),
        ('D', 'Documental'),
        ('A', 'Audible'),
    }
    type = models.CharField(max_length=30, choices=VHS_TYPE, null=False)
    description = models.CharField(max_length=300, null=False)
    price = models.DecimalField(decimal_places=4, max_digits=6)
    picture = models.ImageField(upload_to="catalogo_images")
    
    def __str__(self):
        return self.title
    
class VideoEquipments(models.Model):
    title = models.CharField(max_length=30, null=False)
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)
    description = models.CharField(max_length=300, null=False)
    price = models.DecimalField(decimal_places=4, max_digits=6)
    picture = models.ImageField(upload_to="catalogo_images")

    def __str__(self):
        return self.title