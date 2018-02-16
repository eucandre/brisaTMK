#Cria as rotas do sistema

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app_base.views import *
from app_usuario.views import *
from app_clientes.views import *
from app_equipe.views import *
from django.contrib.auth import views as auth_views
from chat.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', apresentacao),
    url(r'^CriaUsuario',Cria_usuario),
    url(r'^lista_usuarios',lista_usuarios),
    url(r'^edita_usuario/(?P<nr_item>\d+)/$', edita_usuario),
    url(r'^item_usuario/(?P<nr_item>\d+)/$', detalha_usuario),
    url(r'^CriaCliente', Cria_Cliente),
    url(r'^lista_clientes',lista_cliente),
    url(r'^item_cliente/(?P<nr_item>\d+)/$', detalha_cliente),
    url(r'^Criasegmento', Cria_segmento),
    url(r'^lista_segmentos', lista_segmento),
    url(r'^item_segmento/(?P<nr_item>\d+)/$', detalha_segmento),
    url(r'^CriaGrupo',Cria_Grupo),
    url(r'^lista_grupos', lista_grupo),
    url(r'^item_grupo/(?P<nr_item>\d+)/$', detalha_grupo),
    url(r'^CriaDia',Cria_Dia),
    url(r'^Crialideres',Cria_lideres),
    url(r'^lista_lideres', lista_lideres),
    url(r'^Criapromotores',Cria_promotores),
    url(r'^Criaequipe',Cria_equipe),
    url(r'^CriaJornada',Cria_jornada),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
    url(r'^chat',chat),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
