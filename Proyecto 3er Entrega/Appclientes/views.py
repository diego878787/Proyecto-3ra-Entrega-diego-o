from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Appclientes.models import *
from Appclientes.form import *


def inicios(request):
    
    return render(request,"inicios.html")


def agregar_dpersonales(request):

    if request.method=="POST":
        info_formulario = dpersonalesFormulario(request.POST)

        if info_formulario.is_valid():

            info= info_formulario.cleaned_data
            dpersonales1= dpersonales(nombre=info["nombre"],apellido=info["apellido"], dni=info["dni"],sexo=info["sexo"],fnacimiento=info["fnacimiento"])
            dpersonales1.save()
            return render(request,"inicios.html",)
    else:
        info_formulario = dpersonalesFormulario()
    return render(request,"dpersonales.html",{"formu": info_formulario})



def Agregar_ddomicilio(request):

    if request.method=="POST":
        info_formulario = ddomicilioFormulario(request.POST)

        if info_formulario.is_valid():

            info= info_formulario.cleaned_data
            ddomicilio1= ddomicilio(direccion=info["direccion"],localidad=info["localidad"], provincia=info["provincia"],codigopostal=info["codigopostal"])
            ddomicilio1.save()
            return render(request,"inicios.html",)
    else:

        info_formulario = ddomicilioFormulario()
    return render(request,"ddomicilio.html",{"formu": info_formulario})


def Agregar_dcontacto(request):
    
    if request.method=="POST":
        info_formulario = dcontactoFormulario(request.POST)

        if info_formulario.is_valid():

            info= info_formulario.cleaned_data
            dcontacto1= dcontacto(telefonofijo=info["telefonofijo"],telcelular=info["telcelular"], celectronico=info["celectronico"])
            dcontacto1.save()
            return render(request,"inicios.html",)
    else:

        info_formulario = dcontactoFormulario()
    return render(request,"dcontacto.html",{"formu": info_formulario})

   
def Agregar_dproducto(request):
    
    if request.method=="POST":
        info_formulario = productosFormulario(request.POST)

        if info_formulario.is_valid():

            info= info_formulario.cleaned_data
            ddomicilio1= productos(producto=info["producto"],color=info["color"], cantidad=info["cantidad"])
            ddomicilio1.save()
            return render(request,"inicios.html",)
    else:

        info_formulario = productosFormulario()
    return render(request,"dproducto.html",{"formu": info_formulario})

def busqueda_dpersonal_nombre(request):

    return render(request,"inicios.html")
    
def resultado(request):
    
    if request.GET["nombres"]:
        
        nombre = request.GET["nombres"]
        apellidos = dpersonales.objects.filter(nombre__icontains=nombre)

        return render(request,"inicios.html", {"apellido":apellidos, "nombre":apellidos})
        
    else:
        return render(request,"inicios.html")


    



    

 
   

