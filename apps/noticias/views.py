from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Noticia, Categoria
from .forms import Form_Alta, Form_Modificacion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin


class CrearNoticia(LoginRequiredMixin,UserPassesTestMixin, CreateView):
	model = Noticia
	form_class = Form_Alta
	template_name = 'noticias/crear.html'
	success_url = reverse_lazy('noticias:listar_emprendimientos')
	def test_func(self):
		return self.request.user.is_staff
	
	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticia, self).form_valid(form)


def Emprendimientos(request):
	ctx = {}
	categorias = Categoria.objects.all()
	#CAPUTRAR PARAMETROS
	filtro = request.GET.get('fl',None)
	orden = request.GET.get('orden',None)
	if filtro:
		if filtro == 'todas':
			todas_noticias = Noticia.objects.all()
		else:
			cat_filtro = Categoria.objects.filter(nombre = filtro)
			if cat_filtro:
				todas_noticias = Noticia.objects.filter(categoria = cat_filtro[0])
			else:
				todas_noticias = []
				ctx['error'] = "No existe la categoria ingresada."
	else:
		todas_noticias = Noticia.objects.all()

	if orden:
		if orden == 'ala':
			todas_noticias = todas_noticias.order_by('titulo')
		elif orden == 'ald':
			todas_noticias = todas_noticias.order_by('-titulo')
		elif orden == 'ana':
			todas_noticias = todas_noticias.order_by('creado')
		elif orden == 'and':
			todas_noticias = todas_noticias.order_by('-creado')

	ctx['object_list'] = todas_noticias
	ctx['categorias'] = categorias
	return render(request, 'noticias/emprendimientos.html', ctx)



def DetalleNoticiaF(request, pk):
	ctx = {}
	
	noti = Noticia.objects.get(id = pk)
	ctx['noticia'] = noti
	return render(request, 'noticias/detalle.html', ctx)

class Categorias(ListView):
	model = Categoria
	template_name = 'noticias/categorias.html'

def Filtro_Categoria(request, pk):
	ctx = {}
	cate = Categoria.objects.get(id = pk)
	
	filtadas = Noticia.objects.filter(categoria = cate)
	ctx['object_list'] = filtadas
	return render(request, 'noticias/emprendimientos.html', ctx)

class BorrarNoticia(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Noticia
	success_url = reverse_lazy('noticias:listar_emprendimientos')
	def test_func(self):
		return self.request.user.is_staff

class ModificarNoticia(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Noticia
	form_class = Form_Modificacion
	template_name = 'noticias/Modificar.html'
	success_url = reverse_lazy('noticias:listar_emprendimientos')
	def test_func(self):
		return self.request.user.is_staff