from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleado_all'
    ),
    path('list-by-area/<shorname>/', 
        views.ListByArea.as_view(),
        name='empleados_area'
    ),
    path('lista-empleado-admin/', 
        views.ListEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('buscar-empleado-trabajo/', views.listByTrabajo.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades/', views.ListHabilidadesEmpleados.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detalle'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
    ),

]