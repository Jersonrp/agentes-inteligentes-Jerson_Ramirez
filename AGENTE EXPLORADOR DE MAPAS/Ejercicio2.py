import random
import time

definir_entorno = [
    [' ', 'O', ' ', ' ', ' '],
    [' ', ' ', ' ', 'O', ' '],
    [' ', 'O', ' ', ' ', ' '],
    ['O', ' ', 'O', ' ', ' '],
    [' ', ' ', ' ', 'O', ' ']
]

posicion_agente = [0, 0]  
visitados = set()
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

def imprimir_entorno():
    for i in range(len(definir_entorno)):
        for j in range(len(definir_entorno[i])):
            if [i, j] == posicion_agente:
                print('A', end=' ')
            else:
                print(definir_entorno[i][j], end=' ')
        print()
    print('\n')

def obtener_movimientos_validos():
    movimientos = []
    for dx, dy in direcciones:
        nueva_x, nueva_y = posicion_agente[0] + dx, posicion_agente[1] + dy
        if 0 <= nueva_x < len(definir_entorno) and 0 <= nueva_y < len(definir_entorno[0]):
            if definir_entorno[nueva_x][nueva_y] != 'O' and (nueva_x, nueva_y) not in visitados:
                movimientos.append((nueva_x, nueva_y))
    return movimientos

def mover_agente():
    movimientos = obtener_movimientos_validos()
    if movimientos:
        nueva_posicion = random.choice(movimientos)
        posicion_agente[0], posicion_agente[1] = nueva_posicion
        visitados.add(tuple(nueva_posicion))
    else:
        print("No hay movimientos disponibles. Exploración detenida.")
        exit()

while True:
    imprimir_entorno()
    mover_agente()
    time.sleep(1)
