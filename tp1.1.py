import random
import numpy as np
import matplotlib.pyplot as plt
import sys


def graficar_frecuencias():
    # Frecuencia
    for i in range(cant_corridas):
        plt.plot(eje_x, frecuencias[i])
    plt.xlabel("Numero de tiradas")
    plt.ylabel("Frecuencia")
    plt.title("Evaluacion de la frecuencia relativa del número elegido sobre el conjunto")
    plt.axhline(y=0.027, color="black") #valor esperado por 1/37
    #plt.ylim([0.0, 1])
    plt.show()


def graficar_promedios():
    for i in range(cant_corridas):
        plt.plot(eje_x, promedios[i])
    plt.xlabel("Numero de tiradas")
    plt.ylabel("Promedio")
    plt.title("Evaluacion del promedio sobre el conjunto de valores aleatorios")
    plt.axhline(y=18, color="black") # promedio esperado
    plt.show()


def graficar_desviaciones_estandar():
    for i in range(cant_corridas):
        plt.plot(eje_x, desviaciones_estandar[i])
    plt.xlabel("Numero de tiradas")
    plt.ylabel("Desviaciones Estandar")
    plt.title("Evaluacion del desvío sobre el conjunto de valores aleatorios")
    plt.axhline(y=np.sqrt(114), color="black")
    plt.show()


def graficar_varianzas():
    for i in range(cant_corridas):
        plt.plot(eje_x, varianzas[i])
    plt.xlabel("Numero de tiradas")
    plt.ylabel("Varianzas")
    plt.title("Evaluacion de la varianza sobre el conjunto de valores aleatorios")
    # plt.ylim([70, 150]) # esta ponderada la medicion
    plt.axhline(y=114, color="black")
    plt.show()


# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 7 or sys.argv[1] != "-t" or sys.argv[3] != "-c" or sys.argv[5] != "-e":
    print("Uso: python tp1.1.py -t <tiradas> -c <corridas> -e <numero elegido>).")
    sys.exit(1)

cant_tiradas = int(sys.argv[2])
cant_corridas = int(sys.argv[4])
numero_elegido = int(sys.argv[6])

corridas = []
promedios = []
desviaciones_estandar = []
frecuencias = []
varianzas = []
for i in range(cant_corridas):
    corridas.append([])
    promedios.append([])
    desviaciones_estandar.append([])
    frecuencias.append([])
    varianzas.append([])
    for m in range(cant_tiradas):
        corridas[i].append(random.randint(0, 36))
        promedios[i].append(np.average(corridas[i]))
        desviaciones_estandar[i].append(np.std(corridas[i]))
        frecuencias[i].append(corridas[i].count(numero_elegido) / len(corridas[i]))
        varianzas[i].append(np.var(corridas[i]))

eje_x = [m+1 for m in range(cant_tiradas)]

graficar_frecuencias()
graficar_promedios()
graficar_desviaciones_estandar()
graficar_varianzas()


