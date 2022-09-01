from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.

def familia(request):
    familiar_1 = Familia(nombre="Diego Said", edad=37, fecha_nacimiento="1985-02-15")
    familiar_2 = Familia(nombre="Gerardo Said", edad=35, fecha_nacimiento="1986-10-14")
    familiar_3 = Familia(nombre="Franco Said", edad=31, fecha_nacimiento="1990-05-31")

    familiar_1.save()
    familiar_2.save()
    familiar_3.save()

    familiares = {
        familiar_1:{
            'nombre': familiar_1.nombre,
            'edad': familiar_1.edad,
            'fecha_nacimiento': familiar_1.fecha_nacimiento
        },
        familiar_2:{
            'nombre': familiar_2.nombre,
            'edad': familiar_2.edad,
            'fecha_nacimiento': familiar_2.fecha_nacimiento
        },
        familiar_3:{
            'nombre': familiar_3.nombre,
            'edad': familiar_3.edad,
            'fecha_nacimiento': familiar_3.fecha_nacimiento
        }
    }

    return render(request,"AppCoder/familia.html", {'familiares':familiares})