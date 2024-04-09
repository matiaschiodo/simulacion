import random
import numpy as np
import matplotlib.pyplot as plt


numero_elegido = 22
cant_corridas = 10
cant_tiradas = 20
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

eje_x = [+1 for _ in range(cant_tiradas)]

for i in range(cant_corridas):
    plt.plot(eje_x, promedios[i])
plt.xlabel("Numero de tiradas")
plt.ylabel("Promedio")
plt.title("Evaluacion del promedio sobre el conjunto de valores aleatorios")
plt.axhline(y=18, color="r")
plt.ylim([0, 36])
plt.show()

for i in range(cant_corridas):
    plt.plot(eje_x, frecuencias[i])
plt.xlabel("Numero de tiradas")
plt.ylabel("Frecuencia")
plt.title("Evaluacion de la frecuencia relativa sobre el conjunto de valores aleatorios")
plt.axhline(y=0.027, color = "r")
plt.ylim([0.0, 1]) # está ponderada
plt.show()

print(corridas)
