import random
import matplotlib.pyplot as plt
import numpy as np
import math

# GENERADORES
def GCL(seed, n, a=2**16, c=3, m=2**31):
  numbers = []
  for _ in range(n):
    seed = (a + c) * seed % m
    entre0y1 = seed / (2**31 - 1)
    numbers.append(entre0y1)
  return numbers

def CuadradosMedios(seed, n):
  numbers = []
  strings = []
  r = seed
  l = len(str(r))
  for _ in range(n):
    x = str(r**2)
    if l % 2 == 0:
        x = x.zfill(l * 2)
    else:
        x = x.zfill(l)
    y = int((len(x) - l) / 2)
    r = int(x[y:y + l])
    numbers.append(r / (10**l))
    strings.append(x)
  return numbers

def PythonRandom(n):
  numbers = []
  for _ in range(n):
    numbers.append(random.random())
  return numbers

# TESTS
def TestChiCuad(numbers, reps, metodo):
	print(f"Test de bondad Chi Cuadrado con metodo {metodo} y {reps} repeticiones")
	observado = []
	esperado = int(reps / 10)
	c = 0.1
	for _ in range(10):
		x = 0
		for num in numbers:
			if (c - 0.1) <= float(num) <= c:
				x += 1
		observado.append(x)
		c += 0.1
	x2 = 0
	for obs in observado:
		x2 += (((obs - esperado)**2) / esperado)
	print("X2 = " + str(x2))

def TestArribaAbajo(numbers, reps, metodo):
  print(f"Test arriba y abajo con metodo {metodo} y {reps} repeticiones")
  x = []
  corridas = 1
  mas = 0
  menos = 0
  med = np.mean(numbers)

  for num in numbers:
    if num >= med:
      x.append("+")
      mas += 1
    else:
      x.append("-")
      menos += 1

  for i in range(1, len(x)):
    if (x[i] != x[i-1]):
      corridas += 1
      
  n = mas+menos
  media = ((2*menos*mas)/(mas+menos))+1
  desviacion = math.sqrt(((2*menos*mas*(2*mas*menos-n))/((n**2)*(n-1))))
  z = (corridas-media)/desviacion
  print("Z <= " + str(z))

def TestRachas(numbers, reps, metodo):
  print(f"Test de rachas con metodo {metodo} y {reps} repeticiones")
  x = []
  cambios = 1
  for i in range(len(numbers)-1):
    if numbers[i+1] >= numbers[i]:
      x.append("+")
    else:
      x.append("-")
  
  for i in range(1, len(x)):
    if (x[i] != x[i-1]):
      cambios += 1
  
  n = len(x)
  media = (2*n-1)/3
  desviacion = math.sqrt((16*n-29)/90)
  z = (cambios-media)/desviacion
  print("Z <= "+ str(z))

# GRÁFICOS
def Graficar(results, metodo):
  plt.scatter(range(len(results)),results, s=3)
  plt.title(f"Generación de números aleatorios con metodo {metodo}")
  plt.xlabel("Cantidad de Números")
  plt.ylabel("Numero obtenido")
  plt.show()

repeticiones = [10000,50000,100000,500000]

# Metodo GCL
for i in repeticiones:
  results = GCL(6666,i)
  Graficar(results, "GCL")
  TestChiCuad(results, i, "GCL")
  TestArribaAbajo(results, i, "GCL")
  TestRachas(results, i, "GCL")

# Metodo Cuadrados Medios
for i in repeticiones:
  results = CuadradosMedios(1234567890,i)
  Graficar(results, "cuadrados medios")
  TestChiCuad(results, i, "cuadrados medios")
  TestArribaAbajo(results, i, "cuadrados medios")
  TestRachas(results, i, "cuadrados medios")

# #Metodo random de Python
for i in repeticiones:
  results = PythonRandom(i)
  Graficar(results, "random de python")
  TestChiCuad(results, i, "random de python")
  TestArribaAbajo(results, i, "random de python")
  TestRachas(results, i, "random de python")
