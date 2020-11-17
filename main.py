import random
from math import exp
import time
from copy import deepcopy

temperatura = 4000

def calcularAmenaza(n):
    '''Combination formular. Es elegir dos reinas en n reinas'''
    if n < 2:
        return 0
    if n == 2:
        return 1
    return (n - 1) * n / 2

def crear_tablero():
    '''Crea un tablero de ajedrez con una reina en una fila'''
    tablero_ajedrez= {}
    temp = list(range(8))#(0,1,2,3,4,5,6,7)
    random.shuffle(temp)  # shuffle para asgurarse que es aleatorio la forma en la que esta ordenada TEMP
    columna = 0

    while len(temp) > 0:#len tamaño del objeto
        fila = random.choice(temp)#elemento random de la lista
        tablero_ajedrez[columna] = fila
        temp.remove(fila)
        columna += 1
    del temp
    return tablero_ajedrez


def valor(tablero_ajedrez):
    '''Calcula cuántos pares de reina se amenazan'''
    amenazan = 0
    m_tablero = {}
    a_tablero = {}

    for column in tablero_ajedrez:
        temp_m = column - tablero_ajedrez[column]
        temp_a = column + tablero_ajedrez[column]
        ##print("m ",temp_m)
        ##print("a ",temp_a)
        if temp_m not in m_tablero:
            m_tablero[temp_m] = 1
        else:
            m_tablero[temp_m] += 1
        if temp_a not in a_tablero:
            a_tablero[temp_a] = 1
        else:
            a_tablero[temp_a] += 1

    for i in m_tablero:
        amenazan += calcularAmenaza(m_tablero[i])
    del m_tablero

    for i in a_tablero:
        amenazan += calcularAmenaza(a_tablero[i])
    del a_tablero

    return amenazan

def simulated_annealing():
    '''Recocido simulado'''
    solucion_encontrada = False
    respuesta = crear_tablero()

    # Para evitar contar cuando no se puede encontrar un estado mejor
    respuesta_costo = valor(respuesta)##Calcular si se atacan entresi las reinas
    #print(respuesta_costo)

    temperatura_aux = temperatura
    sch = 0.99 ##

    while temperatura_aux > 0:
        temperatura_aux *= sch
        successor = deepcopy(respuesta)
        while True:
            index_1 = random.randrange(0, 8 - 1)##random.randrange(start, stop, step)
            index_2 = random.randrange(0, 8 - 1)
            if index_1 != index_2:
                break
        successor[index_1], successor[index_2] = successor[index_2], \
            successor[index_1]  # intercambiar 2 reinas elegidas
        delta = valor(successor) - respuesta_costo
        if delta < 0 or random.uniform(0, 1) < exp(-delta / temperatura_aux):
            respuesta = deepcopy(successor)##copia una copia del objeto original
            respuesta_costo = valor(respuesta)
        if respuesta_costo == 0:
            solucion_encontrada = True
            imprimir_tablero_ajedrez(respuesta)
            break
    if solucion_encontrada is False:
        print("Solucion no encontrada")


def imprimir_tablero_ajedrez(tablero):
    '''Imprime el tablero'''
    for column, row in tablero.items():
        print("{} => {}".format(column, row))


def main():
    #print(list())
    #print(list(range(8)))
    #print(len(list(range(8))))
    start = time.time()
    simulated_annealing()
    print("Corrida en segundos:", time.time() - start)


if __name__ == "__main__":
    main()
