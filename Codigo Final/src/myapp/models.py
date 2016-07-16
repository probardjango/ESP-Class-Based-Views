from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

TIPO_CHOICES = (
        ('CER', 'Cereal'),
        ('FRU', 'Fruta'),
        ('VER', 'Verdura'),
        ('CAP', 'Capricho'),
        )

class ComprarArticulo(models.Model): #single. 
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    receta = models.CharField(max_length=5000, blank=True, null=True)
    tipo_de_comida = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ["-nombre"]

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        view_name = "detail"
        return reverse(view_name, kwargs={"pk": self.id})