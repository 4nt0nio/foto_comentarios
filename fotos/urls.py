from django.conf.urls import patterns, url, include
from . import views

urlpatterns = [
    url(r'^$',views.vista_fotos, name = 'lista_fotos'),
    url(r'^categoria/(?P<pk>[0-9]+)/detalle/$', views.categoria_detalle,name = 'detalle_categoria'),
    url(r'^fotos/$', views.vista_general_fotos, name='vista_general_fotos'),
    url(r'^fotos/(?P<pk>[0-9]+)/comentario/$',views.vista_comentario, name='vista_comentario'),
    url(r'^fotos/nueva/$', views.nueva_imagen, name='nueva_imagen'),
    url(r'^fotos/(?P<pk>[0-9]+)/editar', views.editar_imagen, name='editar_imagen'),
    url(r'^usuario/nuevo$',views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^ingresar/$',views.ingresar, name='ingresar'),
    url(r'^cerrar/$', views.cerrar_sesion,name='cerrar_sesion'),
    url(r'^eliminar_coment/(?P<pk>[0-9]+)/foto/(?P<pk2>[0-9]+)$',views.eliminar_comentario),
    url(r'^eliminar_foto/(?P<pk>[0-9]+)$',views.eliminar_foto),
]
