from __future__ import division
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import numpy as np
from .models import CalculatorURL

h = 0.00925       # Tamaño del paso (Time step)
MAX = 100.0    # Maximo numero de paso
E = 10000.0
L = 4000.0
P = 10000.0
MS = 1600000.0
ME = 600.0
MI = 0.0
HS = 250000.0
HE = 2.0
HI = 8.0
HR = 0.0
alpha = 1.08
delta = 38.0
C = 200000.0
gamma_e = 1.4
gamma_l = 0.8
gamma_p = 1.1
gamma_h = 0.25
mu_e = 1.0
mu_l = 0.4
mu_p = 0.4
mu_m = 0.29
mu_h = 0.000388
F = 0.5
beta_m = 0.66
beta_h = 0.51
theta_m = 0.1
theta_h = 0.2
u_m = 0.0
t0_c = 33.0
dt_c = 8.5
u_mTemporal = 0.0
resultadoRunge = []
resultadoBogacki = []
resultadoDormand = []

# Create your views here.
class CalcuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "calcu/home.html",{})

    def post(self, request, *args, **kwargs):
        global t0_c, dt_c, u_mTemporal, E, L, P, MS, ME, MI, HS, HE, HI, HR
        if request.method == 'POST':
            u_mTemporal = float(request.POST['inputAc'])
            t0_c = float(request.POST['inputT0'])
            dt_c = float(request.POST['inputDeltaA'])
            E = float(request.POST['huevos'])
            L = float(request.POST['larvas'])
            P = float(request.POST['pupas'])
            MS = float(request.POST['mosquitosSuceptibles'])
            ME = float(request.POST['mosquitosExpuestos'])
            MI = float(request.POST['mosquitosInfectados'])
            HS = float(request.POST['humanosSuceptibles'])
            HE = float(request.POST['humanosExpuestos'])
            HI = float(request.POST['humanosInfectados'])
            HR = float(request.POST['humanosRecuperados'])
            inicializador()
            data = {
                "Runge": getResultadoRunge(),
                "Bogacki": getResultadoBogacki()
            }
            global resultadoRunge, resultadoBogacki
            resultadoRunge = []
            resultadoBogacki = []
            return render(request, "calcu/home.html",{'result':data})

def setResultadoRunge(resul):
    global resultadoRunge
    resultadoRunge.append(resul)

def setResultadoBogacki(resul):
    global resultadoBogacki
    resultadoBogacki.append(resul)

def setResultadoDormand(resul):
    global resultadoDormand
    resultadoDormand.append(resul)

def getResultadoRunge():
    global resultadoRunge
    return resultadoRunge

def getResultadoBogacki():
    global resultadoBogacki
    return resultadoBogacki

def ecuacion1(y,M,H, u_m):
    global delta, C, gamma_e, mu_e
    return delta*(1-y[0]/C)*M - (gamma_e + mu_e)*y[0]

def ecuacion2(y,M,H, u_m):
    global gamma_e, gamma_l, mu_l
    return gamma_e*y[0] - (gamma_l+mu_l)*y[1]

def ecuacion3(y,M,H,u_m):
    global gamma_l, gamma_p, mu_p
    return gamma_l*y[1] - (gamma_p+mu_p)*y[2]

def ecuacion4(y,M,H,u_m):
    global F, gamma_p, beta_m, mu_m
    return F*gamma_p*y[2] - (beta_m*y[8]*y[3])/H - (mu_m+u_m)*y[3]

def ecuacion5(y, M, H, u_m):
    global beta_m, theta_m, alpha, mu_m
    return (beta_m*y[8]*y[3])/H - (theta_m + (alpha*mu_m) + u_m)*y[4]

def ecuacion6(y, M, H, u_m):
    global theta_m, mu_m, alpha
    return theta_m*y[4] - (mu_m*alpha + u_m)*y[5]

def ecuacion7(y, M, H, u_m):
    global mu_h, beta_h
    return mu_h*H - (beta_h*y[5]*y[6])/M - mu_h*y[6]

def ecuacion8(y, M, H, u_m):
    global beta_h, theta_h, mu_h
    return (beta_h*y[5]*y[6])/M - (theta_h+mu_h)*y[7]

def ecuacion9(y, M, H, u_m):
    global theta_h, gamma_h, mu_h
    return theta_h*y[7] - (gamma_h+mu_h)*y[8]

def ecuacion10(y, M, H, u_m):
    global gamma_h, mu_h
    return gamma_h*y[8] - mu_h*y[9]

ecuaciones = {
    0: ecuacion1,
    1: ecuacion2,
    2: ecuacion3,
    3: ecuacion4,
    4: ecuacion5,
    5: ecuacion6,
    6: ecuacion7,
    7: ecuacion8,
    8: ecuacion9,
    9: ecuacion10,
}

def inicializador():
    global MAX, h, E, L, P, MS, ME, MI, HS, HE, HI, HR
    yRunge = np.array([E,L,P,MS,ME,MI,HS,HE,HI,HR])
    yBogacki = np.array([E,L,P,MS,ME,MI,HS,HE,HI,HR])
    yDormand = np.array([E,L,P,MS,ME,MI,HS,HE,HI,HR])
    j = 1
    while j*h<=MAX:
        x = j*h
        rungeKutta4(x,yRunge)
        bogackiShampine(x,yBogacki)
        setResultadoRunge([str(x),str(yRunge[8]),u_m])
        setResultadoBogacki([str(x),str(yBogacki[8]),u_m])
        j = j + 1

def rungeKutta4(x, y):
    k1 = np.zeros(10)
    k2 = np.zeros(10)
    k3 = np.zeros(10)
    k4 = np.zeros(10)
    t2 = np.zeros(10)
    t3 = np.zeros(10)
    t4 = np.zeros(10)

    for i in range(10):
        k1[i] = f(x, y, i)
        t2[i] = y[i] + k1[i] * h/2

    for i in range(10):
        k2[i] = f(x + h/2, t2, i)
        t3[i] = y[i] + k2[i] * h/2

    for i in range(10):
        k3[i] = (f(x + h/2, t3, i))
        t4[i] = (y[i] + k2[i] * h)

    for i in range(10):
        k4[i] = (f(x + h, t4, i))
        y[i] = (y[i] + h*(k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])/6)

def bogackiShampine(x, y):
    k1 = np.zeros(10)
    k2 = np.zeros(10)
    k3 = np.zeros(10)
    t2 = np.zeros(10)
    t3 = np.zeros(10)

    for i in range(10):
        k1[i] = f(x, y, i)
        t2[i] = y[i] + k1[i] * h/2

    for i in range(10):
        k2[i] = f(x + h/2, t2, i)
        t3[i] = y[i] + k2[i] * 3 * h/4

    for i in range(10):
        k3[i] = f(x + 3*h/4, t3, i)
        y[i] = y[i] + 2/9 * h * k1[i] + h/3 * k2[i] + 4/9 * h * k3[i]

def f(x, y, i):
    global delta, C, gamma_e, mu_e, gamma_l, mu_l, gamma_p, mu_p, F, beta_m, mu_m, theta_m, mu_h, beta_h, theta_h, gamma_h, u_m,alpha,dt_c,t0_c,u_mTemporal
    M = y[3] + y[4] + y[5]
    H = y[6] + y[7] + y[8] + y[9]
    u_m = 0.0

    if x> t0_c and x< (t0_c + dt_c):
        u_m = u_mTemporal
    return ecuaciones[i](y, M, H, u_m)

def get_data(request, *args, **kwargs):
    data = getResultado()
    return JsonResponse(data1)
