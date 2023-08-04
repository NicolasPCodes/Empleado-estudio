from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
# MODELS
from .models import Empleado
#FORMS
from .forms import EmpleadoForm

class InicioView(TemplateView):
    # VISTA PAGINA INICIO
    # siempre poner este archivo en home, cuando no sea de prueba
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 4 # METODO PARA PAGINACION
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


    
class ListEmpleadosAdmin(ListView):
    template_name = 'empleados/lista_empleados_admin.html'
    paginate_by = 10 # METODO PARA PAGINACION
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        print('=======', str(palabra_clave))
        lista = Empleado.objects.filter(
            # full_name__icontains=palabra_clave
            first_name__icontains=palabra_clave
        )
        print('lista resultado:', lista)
        return lista
    
class ListByArea(ListView):
    # LISTA EMPLEADOS DE UN AREA
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'
    queryset = Empleado.objects.filter(
        departamento__name ='Contabilidad' 
    )

    def get_queryset(self):
        # codigo propio
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista

class listByTrabajo(ListView):
    template_name = 'empleados/by_trabajo.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('trabajo', '')
        lista = Empleado.objects.filter(
            job=palabra_clave
        )
        print(lista)
        return lista

class ListEmpleadosByKword(ListView):
    """     lista empleado por palabra clave    """
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('---------------')
        palabra_clave = self.request.GET.get('kword', '')
        print('=======', str(palabra_clave))
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        print('lista resultado:', lista)
        return lista

class ListHabilidadesEmpleados(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        numero = self.request.GET.get('habilidad', 1)
        empleado = Empleado.objects.get(id= numero)#recupera un unico registro
        return empleado.habilidades.all()
        
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"

    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "empleados/success.html"

class EmpleadoCreateView(CreateView):
    template_name = "empleados/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')#redireccion al terminar
    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')
    # este siempre se ejecutara primero y para interceptar la data se utiliza el request.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('-------------Metodo post-------------')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #logica del proceso
        print('-------------Metodo form valid-------------')
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')
