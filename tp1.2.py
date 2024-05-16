import random
import numpy as np
import matplotlib.pyplot as plt
import sys


def graficar_frecuencia(frecuencias):
    plt.bar(range(len(frecuencias)), frecuencias, align='center', alpha=0.5)
    plt.axhline(y=0.486, color="black", linestyle='--', label="Frecuencia esperada")
    plt.xlabel('Tirada')
    plt.title('Frecuencia de Ganar por tirada')
    plt.legend(loc='upper right')
    plt.show()


def graficar_capital(capitales, capital_inicial):
    plt.plot(capitales)
    plt.xlabel('Tirada')
    plt.title('Evolución de capital por tirada')
    plt.axhline(y=capital_inicial, color="red", linestyle='--', label="Capital Inicial")
    plt.legend(loc='upper right')
    plt.show()

def graficar_capitales(capitales, capital_inicial):
    for i in capitales:
        plt.plot(i)
    plt.xlabel('Numero de Apuesta')
    plt.ylabel('Capital')
    plt.title('Evolución de capital de múltiples corridas por tirada')
    plt.axhline(y=capital_inicial, color="red", linestyle='--', label="Capital Inicial")
    plt.legend(loc='upper right')
    plt.show()


def grafica_porcentaje_ganancias(porcentaje_ganancias_acumulado):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(porcentaje_ganancias_acumulado) + 1), porcentaje_ganancias_acumulado, marker='o')
    plt.xlabel('Número de Corridas')
    plt.ylabel('Porcentaje de Corridas con Ganancias (%)')
    plt.title('Porcentaje de Corridas con Ganancias Acumulado')
    plt.grid(True)
    plt.show()


def apostar(cant_corridas, apuesta_inicial, capital_inicial, cantidad_de_apuestas, estrategia, capital_ilimitado):

    capitales = []
    ganadas_bool = []
    frecuencias = []
    esta_en_ganancia_bool = []
    for i in range(cant_corridas):
        capital = capital_inicial
        apuesta = apuesta_inicial
        apuesta_numero = 0
        indice_fib = 1
        capitales.append([])
        ganadas_bool.append([])
        frecuencias.append([])
        esta_en_ganancia_bool.append([])

        while apuesta_numero < cantidad_de_apuestas:
            if (capital > apuesta or capital_ilimitado):
                tirada, capital, gano = girarRuleta("Rojo", apuesta, capital)
                print(f"{apuesta_numero}. Capital: {capital} - Apostó: {apuesta}")

                if estrategia == "M": apuesta = martingala(gano, apuesta, apuesta_inicial)
                if estrategia == "D": apuesta = dalembert(gano, apuesta, apuesta_inicial)
                if estrategia == "F": apuesta, indice_fib = fibonacci(gano, apuesta_inicial, indice_fib)
                if estrategia == "C": apuesta = constante(apuesta_inicial)
                if estrategia == "MI": apuesta = martingala_inversa(gano, apuesta, apuesta_inicial)
                ganadas_bool[i].append(gano)
                frecuencias[i].append(ganadas_bool[i].count(True) / len(ganadas_bool[i]))
                ultima_frecuencia = ganadas_bool[i].count(True) / len(ganadas_bool[i])
            else:
                frecuencias[i].append(ultima_frecuencia)

            esta_en_ganancia_bool[i].append(capital > capital_inicial)
            capitales[i].append(capital)

            if capital < apuesta and not capital_ilimitado: print(
                f"La próxima apuesta ({apuesta}) es superior al capital ({capital}).")
            apuesta_numero += 1
            if apuesta_numero == cantidad_de_apuestas: print(f"La simulación llegó a {cantidad_de_apuestas} apuestas.")


    porcentaje_ganancias_acumulado = []
    corridas_con_ganancias = 0
    for i, corrida in enumerate(capitales, 1):
        if corrida[cantidad_de_apuestas - 1] > capital_inicial:
            corridas_con_ganancias += 1
        porcentaje_ganancias_acumulado.append((corridas_con_ganancias / i))

    graficar_capital(capitales[0], capital_inicial)
    graficar_frecuencia(frecuencias[0])
    graficar_capitales(capitales, capital_inicial)
    grafica_porcentaje_ganancias(porcentaje_ganancias_acumulado)

    # Calcular el porcentaje de veces que la estrategia resultó en una ganancia o pérdida en cada corrida
    #porcentaje_ganancias_acumulado = []
    #corridas_con_ganancias = 0

    print('uwu')

def girarRuleta(evento, apuesta, capital):
    rojo = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    impar = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    par = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

    tirada = random.randint(0, 36)
    gano = True

    if tirada in range(1, 13) and evento == "Primeros 12":
        capital += apuesta * 2
    elif tirada in range(13, 25) and evento == "Segundos 12":
        capital += apuesta * 2
    elif tirada in range(25, 36) and evento == "Terceros 12":
        capital += apuesta * 2
    elif tirada in range(1, 37, 3) and evento == "Primera Columna":
        capital += apuesta * 2
    elif tirada in range(2, 38, 3) and evento == "Segunda Columna":
        capital += apuesta * 2
    elif tirada in range(3, 39, 3) and evento == "Tercera Columna":
        capital += apuesta * 2
    elif tirada in range(1, 10) and evento == "1 a 18":
        capital += apuesta
    elif tirada in range(19, 37) and evento == "19 a 36":
        capital += apuesta
    elif tirada in impar and evento == "Impares":
        capital += apuesta
    elif tirada in par and evento == "Pares":
        capital += apuesta
    elif tirada in negro and evento == "Negro":
        capital += apuesta
    elif tirada in rojo and evento == "Rojo":
        capital += apuesta
    elif tirada == evento:
        capital += apuesta * 35
    else:
        capital -= apuesta
        gano = False

    print(f"{'Ganó' if gano else 'Perdió'} - Evento: {evento}, Tirada: {tirada}.")
    return tirada, capital, gano


def martingala(gano, apuesta, apuesta_inicial):
    return apuesta_inicial if gano else apuesta * 2


def dalembert(gano, apuesta, apuesta_inicial):
    # Tomamos la unidad en la estrategia es la apuesta inicial
    return max(apuesta_inicial, apuesta - apuesta_inicial) if gano else apuesta + apuesta_inicial


def fibonacci(gano, apuesta_inicial, indice_fibonacci):
    # Tomamos la unidad en la estrategia es la apuesta inicial
    fib = lambda n: pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)

    if gano:
        indice_fibonacci = max(1, indice_fibonacci - 1)
    else:
        indice_fibonacci += 1

    apuesta = apuesta_inicial * fib(indice_fibonacci)

    return apuesta, indice_fibonacci


def constante(apuesta_inicial):
    return apuesta_inicial


def martingala_inversa(gano, apuesta, apuesta_inicial):
    return apuesta * 2 if gano else apuesta_inicial


# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 11 or sys.argv[1] != "-t" or sys.argv[3] != "-c" or sys.argv[5] != "-s" or sys.argv[7] != "-a":
    print("Uso: python tp1.2.py -t <tiradas> -c <corridas> -s <estrategia> -a <tipo de capital>.")
    print("Estrategias: M (Martingala), D (D'Alembert), F (Fibonacci), MI (Martingala Inversa), C (Constante)")
    print("Tipo de capital: I (Infinito), L (Limitado)")
    sys.exit(1)

cant_tiradas = int(sys.argv[2])
cant_corridas = int(sys.argv[4])
estrategia = sys.argv[8].upper()
capital_ilimitado = sys.argv[10].upper() == 'I'

capital_inicial = 500
apuesta_inicial = 10

print(f"Corridas: {cant_corridas} - Tiradas: {cant_tiradas} - Estrategia: {estrategia} - Capital: {'Ilimitado' if capital_ilimitado else capital_inicial}")

apostar(cant_corridas, apuesta_inicial, capital_inicial, cant_tiradas, estrategia, capital_ilimitado)