from django.shortcuts import render,redirect
from .models import Categoria,Flor      
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from .forms import CustomUserForm

# Create your views here.
@login_required(login_url='/login/')
def vacio_carrito(request):
    request.session["carro"]=""
    lista=request.session.get("carrito","")
    return render(request,"core/carrito.html",{'lista':lista})


def home(request):
    return render(request,'core/home.html')

def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>alert('cerro sesion');window.location.href='/';</script>")

@login_required(login_url='/login/')
def agregar_carro(request, id):
    flor=Flor.objects.get(name__contains=id)
    precio=flor.valor
    sesion=request.session.get("carro","")
    arr=sesion.split(";")
    arr2=''
    sw=0
    cant=1
    for f in arr:
        fl=f.split(":")
        if fl[0]==id:
            cant=int(fl[1])+1
            sw=1
            arr2=arr2+str(fl[0])+":"+str(cant)+":"+str(precio)+";"
        elif not fl[0]=="":
            cant=fl[1]
            arr2=arr2+str(fl[0])+":"+str(cant)+":"+str(precio)+";"
    if sw==0:
        arr2=arr2+str(id)+":"+str(1)+":"+str(precio)+";"
    request.session["carro"]=arr2
    floor=Flor.objects.all()
    msg='Flor Agregada'
    return render(request,'core/galeria.html',{'listafloor':floor,'msg':msg})

@login_required(login_url='/login/')
def carrito(request):
    lista=request.session.get("carro","")
    arr=lista.split(";")
    return render(request,"core/carrito.html",{'lista':arr})

def login(request):
    return render(request,'core/login.html')

def login_iniciar(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        p=request.POST.get("txtPass")
        usu=authenticate(request,username=u,password=p)
        if usu is not None and usu.is_active:
            if usu.is_staff:
                auth_login(request, usu)
                arreglo={'nombre':u, 'contrasena':p, 'tipo':'administrador'}
                return render(request,'core/home.html',arreglo)
            else:
                arreglo={'nombre':u, 'contrasena':p, 'tipo':'cliente'}
                return render(request,'core/home.html',arreglo)
        variables={
            'msg':'no existe nada'
        }
    return render(request,'core/login.html',variables)
   
def login_iniciar(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        p=request.POST.get("txtPass")
        usu=authenticate(request,username=u,password=p)
        if usu is not None and usu.is_active:
            auth_login(request, usu)
            return render(request,'core/home.html')
    return render(request,'core/login.html')
    
@permission_required('core.delete_flor', login_url='/login/')
def eliminar_flor(request,id):
    mensaje=''    
    flo=Flor.objects.get(name=id)
    try:
        flo.delete()
        mensaje='Elimino Flor'
    except:
        mensaje='No pudo Eliminar Flor'
    
    floor=Flor.objects.all()
    return render(request,'core/galeria.html',{'listafloor':floor,'msg':mensaje})


def galeria(request):
    floor=Flor.objects.all()
    return render(request, 'core/galeria.html',{'listafloor':floor})


def quienes_somos(request):
    return render(request,'core/quienes_somos.html')

@permission_required('core.add_flor', login_url='/login/')
def formulario2(request):
    cate=Categoria.objects.all()
    if request.POST:
        nombre=request.POST.get("txtNombre")
        estado=request.POST.get("txtEstado")
        valor=request.POST.get("txtValor")
        descripcion=request.POST.get("txtDescripcion")
        stock=request.POST.get("txtStock")
        categoria=request.POST.get("cboCategoria")
        obj_categoria=Categoria.objects.get(name=categoria)
        imagen=request.FILES.get("txtImagen")
        flor=Flor(
            name=nombre,
            estado=estado,
            valor=valor,
            descripcion=descripcion,
            stock=stock,
            categoria=obj_categoria,
            fotografia=imagen,
        )
        flor.save()
        return render(request,'core/formulario2.html',{'lista':cate,'msg':'grabo','sw':True})
    return render(request,'core/formulario2.html',{'lista':cate})

@permission_required('core.add_flor', login_url='/login/')
def formulario(request):
    mensaje=''
    sw=False
    if request.POST:
        accion=request.POST.get("Accion")
        if accion=="Grabar":
            name=request.POST.get("txtCate")
            cali=request.POST.get("txtCalificacion")
            CATE=Categoria(
                name=name,
                calificacion=cali
            )
            CATE.save()
            mensaje='Grabo'    
            sw=True
        if accion=="Eliminar":
            name=request.POST.get("txtCate")
            cate=Categoria.objects.get(name=name)
            cate.delete()
            mensaje='Elimino'
            sw=True

    categorias=Categoria.objects.all()
    return render(request,'core/formulario.html',{'lista':categorias,'msg':mensaje,'sw':True})

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigirlo al inicio
            u=formulario.cleaned_data['username']
            p=formulario.cleaned_data['password1']
            user=authenticate(request,username=u,password=p)
            auth_login(request, user)
            return redirect(to='HOME')
    return render(request, 'core/registrar.html',data)