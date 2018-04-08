from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


from .models import CalculatorURL

# Create your views here.
def sumar(a,b):
    return int(a) + int(b)

resultado = " "
valor1 = " "
valor2 = " "

class CalcuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "calcu/home.html",{})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            a = request.POST['inputA']
            b = request.POST['inputB']
            global valor1
            valor1 = int(a)
            global valor2
            valor2 = int(b)
            resultado = sumar(a,b)
            setResultado(resultado)
            return render(request, "calcu/home.html",{})

def setResultado(resul):
    global resultado
    resultado = resul

def getResultdo():
    global resultado
    return resultado

def getValor1():
    global valor1
    return valor1

def getValor2():
    global valor2
    return valor2

def get_data(request, *args, **kwargs):
    data = {
        "resultado":getResultdo(),
        "valor1": getValor1(),
        "valor2":getValor2(),
    }
    return JsonResponse(data)
