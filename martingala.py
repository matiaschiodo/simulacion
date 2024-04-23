import random

def martingala(apuesta_inicial, capital_maximo, cantidad_de_apuestas):
    capital = capital_maximo
    apuesta = apuesta_inicial
    numero = 0

    while capital > 0 and numero < cantidad_de_apuestas:
        numero += 1
        resultado = random.randint(0, 36)  # Simula el giro de la ruleta

        if resultado % 2 == 0:  # Si el resultado es par, ganas
            capital += apuesta
            apuesta = apuesta_inicial  # Restablece la apuesta inicial
            print(f"Gano, capital actual: {capital} - Apuesta Nro: {numero}")
        else:  # Si el resultado es impar, pierdes
            capital -= apuesta
            apuesta *= 2  # Duplica la apuesta
            print(f"Perdio, capital actual: {capital} - Apuesta Nro: {numero}")

    return capital, numero


import random

def dalembert(apuesta_inicial, capital_maximo, cantidad_de_apuestas):
    capital = capital_maximo
    apuesta = apuesta_inicial
    numero = 0

    while capital > 0 and numero < cantidad_de_apuestas:
        numero += 1
        resultado = random.randint(0, 36)  # Simula el giro de la ruleta

        if resultado % 2 == 0:  # Si el resultado es par, ganas
            capital += apuesta
            apuesta = max(apuesta - 1, 1)  # Reduce la apuesta
            print(f"Gano, capital actual: {capital} - Apuesta Nro: {numero}")
        else:  # Si el resultado es impar, pierdes
            capital -= apuesta
            apuesta += 1  # Aumenta la apuesta
            print(f"Perdio, capital actual: {capital} - Apuesta Nro: {numero}")

    return capital, numero

apuesta_inicial = 10000
capital_inicial = 100000
cantidad_de_apuestas = 2000

print(f"Capital inicial: {capital_inicial}")
#capital_final, numero_jugadas = martingala(apuesta_inicial, capital_inicial, cantidad_de_apuestas)
capital_final, numero_jugadas = dalembert(apuesta_inicial,capital_inicial,cantidad_de_apuestas)
print(f"Capital final: {capital_final}")
print(f"Ganancia Neta: {capital_final - capital_inicial}")
print(f"Número de jugadas: {numero_jugadas}")

