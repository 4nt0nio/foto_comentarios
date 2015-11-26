from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Foto, Categoria, Cometario
from .forms import FotoForm, CometarioForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout



def vista_fotos(request):
	fotoss = Foto.objects.all()
	cat = Categoria.objects.all()
	return render(request, 'fotos/fotos_todos.html',{'fotos': fotoss,'cate':cat})

def vista_general_fotos(request):
	fotoss = Foto.objects.all()
	cat = Categoria.objects.all()
	return render(request, 'fotos/foto_vista_general.html',{'fotos': fotoss,'cate':cat})

def categoria_detalle(request,pk):
	category =  get_object_or_404(Categoria,pk = pk)
	cat = Categoria.objects.all()
	return render(request, 'fotos/categoria_detalle.html', {'categoria': category,'cate':cat})

def vista_comentario(request,pk):
	comentar = get_object_or_404(Foto,pk = pk)
	cat = Categoria.objects.all()
	if request.method == "POST":
		comentario = CometarioForm(request.POST)
		if comentario.is_valid():
			comentario = comentario.save(commit=False)
			comentario.foto = comentar
			comentario.save()
			return redirect('fotos.views.vista_comentario', pk=pk)
	else:
		comentario = CometarioForm(instance=comentar)
	return render(request, 'fotos/fotos_comentario.html', {'foto': comentar,'formulario':comentario,'cate':cat})


@login_required(login_url='/ingresar')
def nueva_imagen(request):
	cat = Categoria.objects.all()

	if request.method == "POST":
		formulario = FotoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario = formulario.save(commit=False)
			formulario.autor = request.user
			formulario.save()
			return redirect('fotos.views.vista_comentario', pk=formulario.pk)
	else:
		formulario = FotoForm()
	return render(request, 'fotos/editar_imagen.html', {'formulario': formulario,'cate':cat})

@login_required(login_url='/ingresar')
def editar_imagen(request, pk):
	fotos = get_object_or_404(Foto, pk = pk)
	cat = Categoria.objects.all()
	if request.method == "POST":
		form = FotoForm(request.POST, request.FILES,instance=fotos)
		if form.is_valid():
			foto = form.save(commit=False)
			foto.autor = request.user
			foto.save()
			return redirect('fotos.views.vista_comentario', pk=foto.pk)
	else:
		form = FotoForm(instance=fotos)
	return render(request, 'fotos/editar_imagen.html', {'formulario': form,'cate':cat})


def nuevo_usuario(request):
	cat = Categoria.objects.all()
	if request.method == "POST":
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render(request, 'fotos/usuario_nuevo.html',{'formulario': formulario,'cate':cat})



def ingresar(request):
	cat = Categoria.objects.all()
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method == "POST":
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					return render(request, 'fotos/usuario_noactivo.html')
			else:
				return render(request, 'fotos/usuario_noexiste.html')
	else:
		formulario = AuthenticationForm()
		return render(request,'fotos/usuario_autenticar.html', {'formulario': formulario,'cate':cat})



@login_required(login_url='/ingresar')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required(login_url='/ingresar')
def eliminar_comentario(request,pk,pk2):
	coment = get_object_or_404(Cometario, pk = pk).delete()

	return redirect('fotos.views.vista_comentario', pk=pk2)


@login_required(login_url='/ingresar')
def eliminar_foto(request,pk):
	coment = get_object_or_404(Foto, pk = pk).delete()

	return redirect('fotos.views.vista_fotos')