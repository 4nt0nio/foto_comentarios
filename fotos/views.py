from django.shortcuts import render
from django.http import HttpResponse
from .models import Foto, Categoria, Cometario
from django.shortcuts import render, get_object_or_404
from .forms import FotoForm, CometarioForm
from django.shortcuts import redirect


def vista_fotos(request):
	fotoss = Foto.objects.all()
	return render(request, 'fotos/fotos_todos.html',{'fotos': fotoss})

def categorias(request):
	categoriaslist = Categoria.objects.all()
	return render(request, 'fotos/categoria.html', {'categorias': categoriaslist})

def categoria_detalle(request,pk):
	category =  get_object_or_404(Categoria,pk = pk)
	return render(request, 'fotos/categoria_detalle.html', {'categoria': category})

def vista_comentario(request,pk):
	comentar = get_object_or_404(Foto,pk = pk)
	return render(request, 'fotos/fotos_comentario.html', {'foto': comentar})

def nueva_imagen(request):
	if request.method == "POST":
		formulario = FotoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario = formulario.save(commit=False)
			formulario.autor = request.user
			formulario.save()
			return redirect('fotos.views.vista_comentario', pk=formulario.pk)
	else:
		formulario = FotoForm()
	return render(request, 'fotos/editar_imagen.html', {'formulario': formulario})


def editar_imagen(request, pk):
	fotos = get_object_or_404(Foto, pk = pk)
	if request.method == "POST":
		form = FotoForm(request.POST, instance=fotos)
		if form.is_valid():
			foto = form.save(commit=False)
			foto.autor = request.user
			foto.save()
			return redirect('fotos.views.vista_comentario', pk=foto.pk)
	else:
		form = FotoForm(instance=fotos)
	return render(request, 'fotos/editar_imagen.hmtl', {'formulario': form})

def agregar_comentario(request, pk):
	instnacia = get_object_or_404(Foto, pk = pk)
	if request.method == "POST":
		comentario = CometarioForm(request.POST)
		if comentario.is_valid():
			comentario = comentario.save(commit=False)
			comentario.foto = instnacia
			comentario.save()
			return redirect('fotos.views.vista_comentario', pk=pk)
	else:
		form = CometarioForm()
	return render(request, 'fotos/fotos_comentar.html', {'formulario': form})