from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('nuestrosProfesionales/', nuestrosProfesionales, name="nuestrosProfesionales"),
    path('mantenedor/profesional/agregar/', agregar_profesional, name="agregar_profesional"),
    path('mantenedor/profesional/listar/', listar_profesional, name="listar_profesional"),
    path('mantenedor/profesional/modificar/<rut>/', modificar_profesional, name="modificar_profesional"),
    path('mantenedor/profesional/eliminar/<rut>/', eliminar_profesional, name="eliminar_profesional"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro_profesional/', registro_profesional, name="reg_profesional"),
    path('agregar_atencion/', agregar_atencion, name="agregar_atencion"),
    path('ver_profesional/', ver_profesional, name="ver_profesional"),
    path('base/', base_vista, name='base'),
    path('atenciones/listarAtencion/', mis_atenciones, name='mis_atenciones'),
    path('galeria_atenciones/', galeria_atenciones, name="galeria"),
    path('atencion/<int:atencion_id>/', ver_atencion, name='ver_atencion'),
    path('atencion/editar/<int:atencion_id>/', editar_atencion, name='editar_atencion'),
    path('atenciones-en-espera/', atenciones_en_espera, name='atenciones_en_espera'),
    path('atencion/aprobar/<int:atencion_id>/', aprobar_atencion, name='aprobar_atencion'),
    path('atencion/rechazar/<int:atencion_id>/', rechazar_atencion, name='rechazar_atencion'),
    path('trabaja-con-nosotros/', trabajaConNostros, name='trabajaConNosotros'),
    path('postulaciones/', listarPostulacion, name='listar_postulaciones'),
    path('ver-postulacion/<int:pk>/', detallePostulacion, name='detalle_postulacion'),

]   
