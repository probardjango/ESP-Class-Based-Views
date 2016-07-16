from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator

from .forms import CompraModelForm
from .models import ComprarArticulo

Create your views here.
def home(request):
	template = "home.html"
	context = {}
	return render(request, template, context)

def lista(request):
    template = "lista.html"
    queryset = ComprarArticulo.objects.all()
    context = {
        "queryset": queryset
    }
    return render(request, template, context)


def detail(request, pk=None):
	producto = get_object_or_404(ComprarArticulo, pk=pk)
	template = "detail.html"
	context = {
		"titulo": "SOBRE EL PRODUCTO",
		"objeto": producto
	}

	return render(request, template, context)


@login_required (login_url='/admin/')
def create(request):
    form = CompraModelForm(request.POST or None)
    template = "form.html"
    context = {
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        #codigo
        instance.save()
        return redirect(instance) 
    return render(request, template, context)


@login_required(login_url='/admin/')
def update(request, pk=None):
	producto = get_object_or_404(ComprarArticulo, pk=pk)
	form = CompraModelForm(request.POST or None, instance=producto)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	template = "update.html"
	if request.method == 'POST':
		producto.save()
		return HttpResponseRedirect("/lista/")
	context = {
		"objeto": producto,
		"form": form,
		}
	return render(request, template, context)


@login_required(login_url='/admin/')
def delete(request, pk):
	producto = get_object_or_404(ComprarArticulo, pk=pk)
	template = "delete.html"
	
	if request.method == 'POST':
		producto.delete()
		return HttpResponseRedirect("/lista/")
	
	context = {
		"objeto": producto
		}
	return render(request, template, context)