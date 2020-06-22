from django.db import models
from autoslug import AutoSlugField
from usuarios.models import Usuario

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='titulo',unique=True)

    def __str__(self):                                                                               
        return self.titulo

class Subcategoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria,related_name='productos',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='titulo',unique=True)

    def __str__(self):                                                                               
        return self.titulo

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(Subcategoria, related_name='sub_categoria',on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,related_name='usuario_producto',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200,null=True,blank=True)
    descripcion = models.TextField(max_length=1000)
    precio=models.DecimalField(max_digits=12,decimal_places=0)
    imagen = models.ImageField(upload_to='producto-%Y-&m')
    slug = AutoSlugField(populate_from='titulo',unique=True)

    def __str__(self):                                                                               
        return self.titulo
# Create your models here.
