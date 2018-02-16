from __future__ import unicode_literals

from django.db import models

PERFIL = ((u'Administrador do Sistema','Administrador do Sistema'),(u'Lider da Equipe','Lider da Equipe'),
          (u'Promotor de Vendas','Promotor de Vendas'))

class Perfil(models.Model):
    nome = models.CharField(max_length=150, choices=PERFIL)

    def __unicode__(self):
        return self.nome.__str__()

    class Meta:
        verbose_name_plural = 'Perfil de acesso ao sistema'

