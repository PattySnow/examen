from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def index(request):
    atenciones_aprobadas = Atencion.objects.filter(estado=1).order_by('-id')[:5]  # Obtener las últimas 5 atenciones aprobadas

    

    context = {
        'atenciones_aprobadas': atenciones_aprobadas,
       
    }

    return render(request, 'index.html', context)




def base(request): 


    return render(request, "base.html")

       


def contacto(request):
    data = {
        'form': ContactoForm(),
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = ContactoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrió un error"

    return render(request, "contacto.html", data)




def nuestrosProfesionales(request):
    valor_buscado = request.GET.get('valor_buscado', '')
    profesionales = Profesional.objects.none()

    if valor_buscado:
        # Realiza la búsqueda por nombre o por rut del profesional
        profesionales_nombre = Profesional.objects.filter(nombre__icontains=valor_buscado)
        profesionales_rut = Profesional.objects.filter(rut__icontains=valor_buscado)
        profesionales = profesionales_nombre | profesionales_rut
    else:
        # Si no se proporciona un valor de búsqueda, muestra todos los profesionales
        profesionales = Profesional.objects.all()

    context = {
        'valor_buscado': valor_buscado,
        'profesionales': profesionales,
    }
    return render(request, "nuestrosProfesionales.html", context)


def agregar_profesional(request):
    data = {
        'form': ProfesionalForm(),
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = ProfesionalForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Profesional guardado exitosamente"

            # Redireccionar a una página de confirmación o a otra vista
            redirect("mantenedor/profesional/agregar.html")

        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrió un error al guardar el profesional"

    return render(request, "mantenedor/profesional/agregar.html", data)

def listar_profesional(request):
    
    profesionales = Profesional.objects.all()

    data = {
        'profesionales': profesionales
    }

    return render(request,"mantenedor/profesional/listar.html", data)

def modificar_profesional(request, rut):

    profesional = get_object_or_404(Profesional, rut=rut)

    data={
        "form": ProfesionalForm(instance=profesional)
    }

    if request.method == "POST":
        formulario= ProfesionalForm(data = request.POST, instance=profesional, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_profesional")
        else:
            data['form'] = formulario
            data['mensaje'] = "ocurrio un error"

    return render(request,"mantenedor/profesional/modificar.html", data)



def eliminar_profesional(request, rut):

    profesional = get_object_or_404(Profesional, rut=rut)

    profesional.delete()

    return redirect(to=listar_profesional)



def login_usuario(request):


    print('grupos:', request.user.groups.all())

    if request.user.groups.filter(name=['Mecanico']):
        print('Usuario Mecanico')

    return redirect(to='index')

def es_administrador(user):
    return user.groups.filter(name='AdministradorTaller').exists()

def is_mecanico(user):
    return user.groups.filter(name='Mecanico').exists()


@login_required(login_url='/accounts/login')
@user_passes_test(es_administrador, login_url='/accounts/login')
def registro_profesional(request):
    data = {
        "mensaje": ""
    }

    es_administrador = request.user.groups.filter(name='AdministradorTaller').exists()
    context = {
        'es_administrador': es_administrador,
    }

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        rut = request.POST.get("rut")
        foto = request.FILES.get("foto")

        if password1 != password2:
            data['mensaje'] = "La contraseña no coincide"
        else:
            try:
                # Crear una instancia de User
                user = User.objects.create_user(username=correo, password=password1, email=correo,
                                                first_name=nombre, last_name=apellido)
                # Asociar al grupo 'Mecanico'
                grupo = Group.objects.get(name='Mecanico')
                user.groups.add(grupo)

                # Crear una instancia de Profesional y asociarla con la instancia de User
                profesional = Profesional.objects.create(nombre=nombre, apellidoPaterno=apellido, correo=correo, usuario=user)
                profesional.rut = rut
                profesional.foto = foto
                profesional.save()
                data['mensaje']="Mecanico registrado exitosamente"

              

            except Exception as e:
                data['mensaje'] = 'Error al guardar: ' + str(e)

    return render(request, "registration/registro.html", {**data, **context})





@login_required
def agregar_atencion(request):
    data = {
        'form': AtencionForm(),
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = AtencionForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            atencion = formulario.save(commit=False)
            atencion.mecanico = request.user.profesional
            atencion.save()
            data['mensaje'] = "Atención guardada"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrió un error"

    return render(request, "mantenedor/atenciones/agregarAtencion.html", data)



def ver_profesional(request):

    return render(request,"perfilMecanico.html" )

def base_vista(request):
    tiene_permiso = request.user.has_perm("appweb.view_atencion")
    print("tiene_permiso:", tiene_permiso)
    return render(request, 'base.html', {'tiene_permiso': tiene_permiso})

@login_required
def mis_atenciones(request):
    # Obtener el mecanico actualmente autenticado
    mecanico = request.user.profesional

    # Obtener las atenciones asociadas al mecanico y ordenarlas por fecha de creación descendente
    atenciones = Atencion.objects.filter(mecanico=mecanico).order_by('-id')

    data = {
        'atenciones': atenciones,
        'mensaje': ""
    }

    return render(request, "mantenedor/atenciones/listarAtencion.html", data)



def galeria_atenciones(request):
    valor_buscado = request.GET.get('valor_buscado', '')

    atenciones_aprobadas = Atencion.objects.filter(estado=1).order_by('-id')

    if valor_buscado:
        categorias = [categoria[1] for categoria in Categoria if valor_buscado.lower() in categoria[1].lower()]
        atenciones = atenciones_aprobadas.filter(
            Q(mecanico__nombre__icontains=valor_buscado) |
            Q(mecanico__apellidoPaterno__icontains=valor_buscado) |
            Q(categoria__in=categorias)
        )
    else:
        atenciones = atenciones_aprobadas

    context = {
        'valor_buscado': valor_buscado,
        'atenciones': atenciones,
    }
    return render(request, 'galeria_atenciones.html', context)











def ver_atencion(request, atencion_id):
    atencion = get_object_or_404(Atencion, pk=atencion_id)
    context = {
        'atencion': atencion
    }
    return render(request, 'mantenedor/atenciones/verAtencion.html', context)



def editar_atencion(request, atencion_id):
    atencion = get_object_or_404(Atencion, pk=atencion_id)
    form = AtencionForm(request.POST or None, instance=atencion)

    mensaje = ''  # Inicializamos el mensaje

    if request.method == 'POST':
        if form.is_valid():
            if atencion.estado == 2:  # Verifica si el estado es "Rechazada"
                atencion.estado = 0  # Cambia el estado a "En Espera"
            form.save()
            # Realiza cualquier otra acción necesaria después de guardar los cambios
            mensaje = 'Cambios Guardados'
        else:
            mensaje = 'Formulario inválido'

    context = {
        'atencion': atencion,
        'form': form,
        'mensaje': mensaje,  # Pasamos el mensaje al contexto
    }

    return render(request, 'mantenedor/atenciones/editarAtencion.html', context)


def atenciones_en_espera(request):
    atenciones_en_espera = Atencion.objects.filter(estado=0)  # Filtrar por estado "En Espera"

    context = {
        'atenciones': atenciones_en_espera,
    }

    return render(request, 'mantenedor/atenciones/atenciones_en_espera.html', context)




def aprobar_atencion(request, atencion_id):
    atencion = get_object_or_404(Atencion, id=atencion_id)

    if request.method == 'POST':
        # Cambiar el estado a 'Aprobada'
        atencion.estado = 1  # Asignar el valor correspondiente a "Aprobada" según la configuración de opciones
        atencion.save()
        # Realizar otras acciones necesarias después de aprobar la atención

        return redirect('atenciones_en_espera')  # Redirigir a la página de peticiones en espera

    context = {
        'atencion': atencion
    }

    return redirect('atenciones_en_espera')



def rechazar_atencion(request, atencion_id):
    atencion = get_object_or_404(Atencion, id=atencion_id)

    if request.method == 'POST':
        motivo_rechazo = request.POST.get('motivo_rechazo')
        if motivo_rechazo:
            atencion.estado = 2  # Asignar el valor correspondiente a "Rechazada" según la configuración de opciones
            atencion.motivoRechazo = motivo_rechazo
            atencion.save()
            # Realizar otras acciones necesarias después de rechazar la atención

    return redirect('atenciones_en_espera')

def trabajaConNostros(request):
    data = {
        'form': TrabajaConNosotrosForm(),
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = TrabajaConNosotrosForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Postulacion enviada"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"
    return render(request, "trabajaConNosotros.html", data)



def listarPostulacion(request ):
    
    formulario = TrabajaConNosotros.objects.all()

    data = {
        'formulario': formulario
    }

    return render(request, "mantenedor/postulaciones/listarPostulaciones.html", data)

def detallePostulacion(request, pk):
    formulario = get_object_or_404(TrabajaConNosotros, pk=pk)
    data = {
        'formulario':formulario
    }
    return render(request, "verPostulacion.html", data)








