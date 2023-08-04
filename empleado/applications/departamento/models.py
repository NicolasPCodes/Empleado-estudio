from django.db import models

# Create your models here.
class Departamento(models.Model):
    #   Modelo para tabla departamento
    name = models.CharField('Nombre', max_length=50,)
    short_name = models.CharField('Nombre Corto', max_length=20, unique= True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']#ordenar segun nombre pero al revez 
        unique_together = ('name', 'short_name')#caracter unico a registrar

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name 
