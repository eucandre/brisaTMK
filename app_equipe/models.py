# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from app_usuario.models import *

DIAS = ((u'Segunda-feira','Segunda-feira'), (u'Terca-feira','Terca-feira'), (u'Quarta-feira','Quarta-feira'), (u'Quinta-feira','Quinta-feira')
        , (u'Sexta-feira','Sexta-feira'), (u'Sabado','Sabado'))

PERIODO= ((u'Manha', 'Manha'), (u'Tarde', 'Tarde'), (u'Manha e Tarde','Manha_e_Tarde'))



class Dias(models.Model):
    dia = models.CharField(choices=DIAS,max_length=150)

    def __unicode__(self):
        return self.dia.__str__()

    class Meta:
        verbose_name_plural = 'Dias da semana de jornada'

class Lideres(models.Model):
    '''
    Classe que cadastra todos os líderes de equipes
    '''
    lideres = models.ManyToManyField(User)

    def __unicode__(self):
        return self.lideres.__str__()

    class Meta:
        verbose_name_plural = 'Lideres de Equipes'

class Promotores(models.Model):
    '''
    Classe que cadastra todos os promotores de vendas
    '''
    promotores = models.ManyToManyField(User)

    def __unicode__(self):
        return self.promotores.__str__()

    class Meta:
        verbose_name_plural = 'Promotores de vendas'

class Equipe(models.Model):
    '''
    Classe que registra as equipes com ses respectivos líderes e promotores de venda

    '''
    nome= models.CharField(max_length=150)
    lideres = models.ManyToManyField(Lideres)
    promotores = models.ManyToManyField(Promotores)

    def __unicode__(self):
        return self.nome.__str__()

    class Meta:
        verbose_name_plural = 'Equipe'

class Jornada(models.Model):
    '''
    Classe que cadastra a jornada de trabalho da equipe.
    Esta jornada de trabalho irá redigir o colaborador.
    '''
    nome = models.CharField(max_length=150)
    jornada_equipe=models.ForeignKey(User)
    dias_jornada =models.ManyToManyField(Dias)
    periodo = models.CharField(choices=PERIODO, max_length=150)
    de = models.TimeField()
    ate = models.TimeField()

    def __unicode__(self):
        return self.jornada_equipe.__str__()

    class Meta:
        verbose_name_plural = 'Jornada de Trabalho'



