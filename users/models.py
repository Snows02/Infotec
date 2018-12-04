from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    document = models.CharField(
        'Documento de identidad',
        max_length=15,
        null=False,
        blank=False
    )
    fecha_nacimiento = models.DateField(default= '2018-10-27')

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


    def __str__(self):
        return "%s %s"%(self.user.first_name, self.user.last_name)

