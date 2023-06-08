from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
#-------------------------------------
# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | RIVERA CASO </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> INICIO</a>
        </li>
        <li>
            <a href="/saludo"> MENSAJE DE SALUDO</a>
        </li>
        <li>
            <a href="/rango"> MOSTRAR NÚMEROS [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/40"> MOSTRAR NÚMEROS [10,15]</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    return render(request,'index.html')

def saludo(request):
    return render(request,'saludo.html')

def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """

    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)

def rango2(request,a=10,b=40):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)



#------------------------------------------------
