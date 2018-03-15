#Cria as rotas do sistema

from django.conf.urls import *
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from app_usuario.views import *
from app_equipe.views import *
from app_base.views import *
from app_cliente.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Show),
    # url(r'^CriaUsuario',Cria_usuario),
    url(r'^lista_usuarios',lista_usuarios),
    # url(r'^edita_usuario/(?P<nr_item>\d+)/$', edita_usuario),
     url(r'^item_usuario/(?P<nr_item>\d+)/$', detalha_usuario),
     url(r'^CriaCliente', Cria_Cliente),
     url(r'^lista_clientes',lista_clientes),
     url(r'^item_cliente/(?P<nr_item>\d+)/$', detalha_Cliente),
     url(r'^Criasegmento', Cria_segmento),
     url(r'^lista_segmentos', lista_segmento),
     #url(r'^item_segmento/(?P<nr_item>\d+)/$', detalha_segmento),
    url(r'^CriaGrupo',Cria_Grupo),
    url(r'^lista_grupos', lista_grupo),
    url(r'^item_grupo/(?P<nr_item>\d+)/$', detalha_Grupo),
    url(r'^edita_grupo/(?P<nr_item>\d+)/$', edita_grupo),
    # url(r'^CriaDia',Cria_Dia),
     url(r'^Crialideres',Cria_Lider),
    # url(r'^lista_lideres', lista_lideres),
     url(r'^CriaColaborador',Cria_Colaborador),
     url(r'^Criaequipe',Cria_Equipe),
     url(r'^lista_equipe',lista_equipe),
     url(r'^item_lider/(?P<nr_item>\d+)/$', detalha_lider),
     url(r'^item_colaborador/(?P<nr_item>\d+)/$', detalha_colaborador),
     url(r'^item_equipe/(?P<nr_item>\d+)/$', detalha_equipe),
    # url(r'^CriaJornada',Cria_jornada),
    # url(r'^deleta_usuario/(?P<nr_item>\d+)/$', delete_usuario),
    url(r'^CriaUsuario', Cria_Usuario),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
    #url(r'^chat',chat),
    #url(r'^accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
