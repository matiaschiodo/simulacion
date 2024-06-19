import random
import matplotlib.pyplot as plt
import  math
import numpy as np
from scipy.stats import norm
import scipy.stats 

def uniforme(a, b):
    x = []
    for i in range(1000):
        r = round(random.random(), 4)
        x.append(a + (b - a) * r)
    return x

uni = uniforme(1, 3)

def TestChiCuadUni(u):
    print("Test de bondad Chi Cuadrado para distribucion uniforme")
    observado = []
    esperado = 100
    c = 1.2
    chiquadesperado = round(scipy.stats.chi2.ppf(1 - 0.05, 9), 2)
    for i in range(10):
        x = 0
        for j in range(len(u)):
            if  (c - 0.2) <= float(u[j]) <= c:
                x += 1
        observado.append(x)
        c += 0.2
    x2 = 0
    for i in range(len(observado)):
        x1 = (((observado[i] - esperado) ** 2) / esperado)
        x2 += x1

    print("Valor de X2 obtenido = " + str(x2))
    print("Se poseen 10 intervalos, por lo tantos tendremos 9 grados de libertad.")
    print("Con 9 grados de libertad y con un 95 porciento de confianza se obtiene un valor de Chi cuadrado de 16.92")
    if (x2 < chiquadesperado):
        print("El valor de chi cuadrado obtenido: " + str(x2) +
              " es menor que " + str(chiquadesperado) + ", por lo tanto Paso el test")
    else:
        print("No paso el test")

def exponencial(ex):
    x = []
    for i in range(1000):
        r = random.random()
        x += [-ex * (np.log(r))]
    return x

expo = exponencial(5)

def TestChiCuadExp(u):
    print("Test de bondad Chi Cuadrado para distribucion exponencial:")
    observado = []
    esperado = []
    c = 0.3
    chiquadesperado = round(scipy.stats.chi2.ppf(1 - 0.05, 9), 2)
    for i in range (9):
        x = 0
        for j in range (len(u)):
             if  (c - 0.3) <= float(u[j]) <= c:
                x+=1
        observado.append(x)
        esperado.append(1000 * ((1 - (math.e) ** (-(1 / 5) * c)) - (1 - (math.e) ** (-(1 / 5) * (c - 0.3)))))
        c += 0.3
    observado.append(1000 - sum(observado))
    esperado.append(1000 * ((math.e) ** (-(1 / 5) * (c - 0.3))))
    x2 = 0
    for i in range(len(observado)):
        x1 = (((observado[i] - esperado[i]) ** 2) / esperado[i])
        x2 += x1
    print("Valor de X2 obtenido = " + str(x2))
    print("Se poseen 10 intervalos, por lo tantos tendremos 9 grados de libertad.")
    print("Con 9 grados de libertad y con un 95 porciento de confianza se obtiene un valor de Chi cuadrado de 16.92")
    if (x2 < chiquadesperado):
        print("El valor de chi cuadrado obtenido: " + str(x2) +
              " es menor que " + str(chiquadesperado) + ", por lo tanto Paso el test")
    else:
        print("No paso el test")

def gamma(k, a):
    x = []
    for i in range(1, 1000):
        tr = 1.0
        for j in range(1, k):
            r = random.random()
            tr = tr * r
        x.append(-(math.log10(tr)) / a)
    return x

gam = gamma(5, 20)

def normal(mu, sigma):
    x = []
    for i in range(1000):
        sum = 0.0
        for j in range (12):
            r = random.random()
            sum += r
        x += [sigma * (sum - 6.0) + mu]
    return x

nor = normal(2.35, 30)

def TestChiCuadNormal(u):
    print("Test de bondad Chi Cuadrado para distribucion Normal")
    observado = []
    esperado = []
    a1 = 0
    a2 = 0
    chiquadesperado = round(scipy.stats.chi2.ppf(1 - 0.05, 9), 2)
    c =- 80
    for i in range(10):
        x = 0
        for j in range(len(u)):
            if (c - 20) <= float(u[j]) <= c:
                x += 1
        observado.append(x)
        a1 += (c - 10) * x
        a2 += ((c - 10) ** 2) * x
        c += 20
    a1 = a1 / 1000
    a2 = a2 / 1000
    desviacion = math.sqrt(a2 - a1 ** 2)
    media = a1
    c =- 80
    esperado = []
    for i in range(10):
        esperado.append (1000 * (norm.cdf((c - media) / desviacion) - norm.cdf(((c - 20) - media) / desviacion)))
        c += 20
    x2 = 0
    for i in range(len(observado)):
        x1 = (((observado[i] - esperado[i]) ** 2) / esperado[i])
        x2 += x1
    print("Valor de X2 obtenido = " + str(x2))
    print("Se poseen 10 intervalos, por lo tantos tendremos 9 grados de libertad.")
    print("Con 9 grados de libertad y con un 95 porciento de confianza se obtiene un valor de Chi cuadrado de 16.92")
    if (x2 < chiquadesperado):
            print("El valor de chi cuadrado obtenido: " + str(x2) +
              " es menor que " + str(chiquadesperado) + ", por lo tanto Paso el test")
    else:
        print("No paso el test")

def pascal(k, q):
    nx = []
    for i in range(1000):
        tr = 1
        qr = math.log10(q)
        for j in range(k):
            r = random.random()
            tr *= r
        x = int(math.log10(tr) // qr)
        nx.append(x)
    return nx
    
pas = pascal(5, 0.4)

def binomial(n, p):
    x = []
    for i in range(1000):
        y = 0.0
        for j in range(1, n):
            r = random.random()
            if (r - p) < 0:
                y += 1.0
        x.append(y)
    return x

bino = binomial(1000, 0.4)

def TestChiCuadBinomial(u):
    print("Test de bondad Chi Cuadrado para distribucion Binomial")
    observado = []
    esperado = []
    X = scipy.stats.binom(1000, 0.4)
    c = 354
    chiquadesperado = round(scipy.stats.chi2.ppf(1 - 0.05, 9), 2)
    for i in range(10):
        x = 0
        for j in range(len(u)):
            if (c - 14) <= float(u[j]) < c:
                x += 1
        observado.append(x)
        total = sum(X.pmf(k) for k in range (c)) -sum(X.pmf(m) for m in range (c - 14))
        esperado.append(1000 * total)
        c += 14   
    x2 = 0
    for i in range(len(observado)):
        x1 = (((observado[i] - esperado[i]) ** 2) / esperado[i])
        x2 += x1

    print("Valor de X2 obtenido = " + str(x2))
    print("Se poseen 10 intervalos, por lo tantos tendremos 9 grados de libertad.")
    print("Con 9 grados de libertad y con un 95 porciento de confianza se obtiene un valor de Chi cuadrado de 16.92")
    if (x2 < chiquadesperado):
        print("El valor de chi cuadrado obtenido: " + str(x2) +
              " es menor que " + str(chiquadesperado) + ", por lo tanto Paso el test")
    else:
        print("No paso el test")
  
def hipergeometrica(tn, ns, p):
    x = []
    for i in range(1000):
        tn1 = tn
        ns1 = ns
        p1 = p
        y = 0.0
        for j in range(1, ns1):
            r = random.random()
            if(r - p1) > 0:
                s = 0.0
            else:
                s = 1.0
                y += 1.0
            p1 = (tn1 * p1 - s) / (tn1 - 1.0)
            tn1 -= 1.0
        x.append(y)
    return x

hipergeo = hipergeometrica(1000, 500, 0.4)

def poisson(lamb):
    x = []
    for i in range(1000):
        cont = 0
        tr = 1
        b = 0
        while(tr - b >= 0):
            b = math.exp(-lamb)
            r = random.random()
            tr=tr * r
            if(tr - b >= 0):
                cont += 1
        x.append(cont)
    return x

poi = poisson(50)

def TestChiCuadPoisson(u):
    print("Test de bondad Chi Cuadrado para distribucion Poisson")
    observado = []
    esperado = []
    X = scipy.stats.poisson(50)
    chiquadesperado = round(scipy.stats.chi2.ppf(1 - 0.05, 9), 2)
    c = 26
    for i in range(10):
        x = 0
        for j in range(len(u)):
            if (c - 6) <= float(u[j]) < c:
                x += 1
        observado.append(x)
        total = sum(X.pmf(k) for k in range (c)) -sum(X.pmf(m) for m in range (c - 6))
        esperado.append(1000 * total)
        c += 6
    x2 = 0
    for i in range(len(observado)):
        x1 = (((observado[i] - esperado[i]) ** 2) / esperado[i])
        x2 += x1
    print("Valor de X2 obtenido = " + str(x2))
    print("Se poseen 10 intervalos, por lo tantos tendremos 9 grados de libertad.")
    print("Con 9 grados de libertad y con un 95 porciento de confianza se obtiene un valor de Chi cuadrado de 16.92")
    if (x2 < chiquadesperado):
        print("El valor de chi cuadrado obtenido: " + str(x2) +
              " es menor que " + str(chiquadesperado) + ", por lo tanto Paso el test")
    else:
        print("No paso el test")

def empirica():
    x = []
    p = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]
    for i in range(1000):
        r = random.random()
        a = 0
        z = 1
        for j in p:
            a += j
            if (r <= a):
                break
            else:
                z += 1
        x.append(z)
    return x

empi = empirica()

def TestChiCuadEmpirica(u):
    print("Test de bondad Chi Cuadrado para distribucion Empirica")
    observado = []
    esperado = []
    chiquadesperado = round(scipy.stats.chi2.ppf(1 - 0.05, 9), 2)
    p = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]
    for i in range(6):
        x = 0
        for j in range(len(u)):
            if u[j] == i + 1:
                x += 1
        observado.append(x)
        esperado.append(1000 * p[i]) 
    x2 = 0
    for i in range(len(observado)):
        x1 = (((observado[i] - esperado[i]) ** 2) / esperado[i])
        x2 += x1

    print("Valor de X2 obtenido = " + str(x2))
    print("Se poseen 10 intervalos, por lo tantos tendremos 9 grados de libertad.")
    print("Con 9 grados de libertad y con un 95 porciento de confianza se obtiene un valor de Chi cuadrado de 16.92")
    if (x2 < chiquadesperado):
        print("El valor de chi cuadrado obtenido: " + str(x2) +
              " es menor que "+ str(chiquadesperado) + ", por lo tanto Paso el test")
    else:
        print("No paso el test")

def graficar(u, g, e, n, p, b, em, pas, hipergeo):
    plt.figure(1)
    plt.title("Uniforme")
    plt.hist(u, color='g')
    plt.savefig("Uniforme.png")
    
    plt.figure(2)
    plt.title("Exponencial")
    plt.hist(e, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='g')
    plt.savefig("Exponencial.png")

    plt.figure(3)
    plt.title("Gamma")
    plt.hist(g, 25, histtype="stepfilled", alpha=.7,linewidth=5, color='g')
    plt.savefig("Gamma.png")

    plt.figure(4)
    plt.title("Normal")
    plt.hist(n, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='g')
    plt.savefig("Normal.png")
    
    plt.figure(5)
    plt.title("Pascal")
    plt.hist(pas, color='g')
    plt.savefig("Pascal.png")
    
    plt.figure(6)
    plt.title("Binomial")
    plt.hist(b, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='g')
    plt.savefig("Binomial.png")
    
    plt.figure(7)
    plt.title("Hipergeometrica")
    plt.hist(hipergeo, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='g')
    plt.savefig("HiperGeometrica.png")

    plt.figure(8)
    plt.title("Poisson")
    plt.hist(p, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='g')
    plt.savefig("Poisson.png")

    plt.figure(9)
    plt.title("Empirica")
    plt.hist(em, color='g')
    plt.savefig("Empirica.png")

graficar(uni, gam, expo, nor, poi, bino, empi, pas, hipergeo)
TestChiCuadUni(uni)
print()
TestChiCuadExp(expo)
print()
TestChiCuadNormal(nor)
print()
TestChiCuadBinomial(bino)
print()
TestChiCuadPoisson(poi)
print()
TestChiCuadEmpirica(empi)

