from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.

def familia(request):
    familiar1 = Familia(nombre="Diego Said", edad=37, fechaNacimiento="1985-02-15")
    familiar2 = Familia(nombre="Gerardo Said", edad=35, fechaNacimiento="14/10/1986")
    familiar3 = Familia(nombre="Franco Said", edad=31, fechaNacimiento="31/05/1990")

    familiar1.save()
    familiar2.save()
    familiar3.save()

    texto1=f"nombre: {familiar1.nombre}, edad: {familiar1.edad} y fecha de nacimiento: {familiar1.fechaNacimiento}"
    texto2=f"nombre: {familiar2.nombre}, edad: {familiar2.edad} y fecha de nacimiento: {familiar2.fechaNacimiento}"
    texto3=f"nombre: {familiar3.nombre}, edad: {familiar3.edad} y fecha de nacimiento: {familiar3.fechaNacimiento}"

    return render(request,"AppCoder/familia.html")