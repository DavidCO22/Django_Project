from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('about/',views.about,name="about"),
    path('database/<int:ids>',views.basedatos),
    path('proyectos/',views.proyectos,name="proyectos"),
    path('task/<str:proj>',views.task,name="task"),
    path('create_task/<str:tipo>',views.create_task,name="create"),
    path('login/',views.log_in,name="login"),
    path('logout/',views.salir,name="logout"),
    path('registro/',views.registro,name="registro"),
    path('tareas/',views.tareas,name="tareas"),
    path('ag_tarea/',views.add_task,name="add_task"),
    path('info_task/<str:tk>',views.info_task,name="info_task"),
    path('delete_task/<str:db>',views.delete_task,name="delete_task"),
    path('edit_task/<str:db>',views.edit_task,name="edit_task")
]