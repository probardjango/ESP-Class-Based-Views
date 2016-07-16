from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


from .forms import CompraModelForm
from .models import ComprarArticulo

#Create your views here.
class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self, request, *args, **kwargs):
		return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class MyAppCreate(CreateView):
	# model = ComprarArticulo
	# fields = ["nombre", "tipo_de_comida"]
	form_class = CompraModelForm
	template_name = "myapp/comprararticulo_form.html"

	def get_success_url(self):
		return reverse("list")

	# def form_valid(self):

class MyAppUpdate(StaffRequiredMixin, UpdateView):
	model = ComprarArticulo
	# fields = []
	form_class = CompraModelForm
	template_name = "myapp/comprararticulo_update.html"

class MyAppDelete(StaffRequiredMixin, DeleteView):
	model = ComprarArticulo

	def get_success_url(self):
		return reverse("list")

class MyAppDetail(DetailView):
	model = ComprarArticulo

class MyAppListView(ListView):
	model = ComprarArticulo

	# def get_queryset(self, *args, **kwargs):
	# 	qs = super(MyAppListView, self).get_queryset(*args, **kwargs)
	# 	return qs


class MyAppTemplateView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, *args, **kwargs):
		context = super(MyAppTemplateView, self).get_context_data(*args, **kwargs)
		context["titulo"] = "EAT THE RAINBOW"
		return context

# def home(request):
# 	template = "home.html"
# 	context = {
# 		"titulo": "Cualquier cosa"
# 	}
# 	return render(request, template, context)

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