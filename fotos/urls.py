from django.conf.urls import patterns, url, include
from . import views

urlpatterns = [
    url(r'^$',views.vista_fotos, name = 'lista_fotos'),
    url(r'^categoria/$',views.categorias, name = 'lista_categoria'),
    url(r'^categoria/(?P<pk>[0-9]+)/detalle/$', views.categoria_detalle,name = 'detalle_categoria'),
    url(r'^fotos/(?P<pk>[0-9]+)/comentario/$',views.vista_comentario, name='vista_comentario'),
    url(r'^fotos/nueva/$', views.nueva_imagen, name='nueva_imagen'),
    url(r'^fotos/(?P<pk>[0-9]+)/editar', views.editar_imagen, name='editar_imagen'),
    url(r'^fotos/(?P<pk>[0-9]+)/comentar', views.agregar_comentario, name='nuevo_comentario'),
]
