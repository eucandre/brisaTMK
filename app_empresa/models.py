from __future__ import unicode_literals

from django.db import models
from app_usuario.models import *



class Dados_na_Empresa(models.Model):
    '''
    dados do clocaborador cadastrados na empresa
    '''
    colaborador = models.ForeignKey(User)
    matricula = models.CharField(max_length=150)
    data_adminissao = models.DateField()
    tipo_remuneracao = models.CharField(max_length=150,choices=((u'Horista','horista'),(u'Mensalista','Mensalista')))

    def __unicode__(self):
        return self.colaborador.__str__()

    class Meta:
        verbose_name_plural = 'Dados do Colaborador na Empresa'