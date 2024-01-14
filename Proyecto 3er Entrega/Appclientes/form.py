from django import forms

class dpersonalesFormulario(forms.Form):
    nombre = forms.CharField (max_length = 30)
    apellido = forms.CharField (max_length = 30)
    dni = forms.IntegerField ()
    sexo = forms.CharField (max_length = 10)
    fnacimiento = forms.DateField ()

class ddomicilioFormulario(forms.Form):
    direccion = forms.CharField (max_length = 40)
    localidad = forms.CharField (max_length = 30)
    provincia = forms.CharField (max_length = 20)
    codigopostal = forms.IntegerField ()

class dcontactoFormulario(forms.Form):
    telefonofijo = forms.CharField (max_length = 20)
    telcelular = forms.IntegerField ()
    celectronico = forms.EmailField ()

class productosFormulario(forms.Form):
    producto = forms.CharField (max_length = 30)
    color = forms.CharField (max_length = 20)
    cantidad = forms.IntegerField ()