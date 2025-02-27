import random
import time

definir_entorno = [
    [' ', ' ', 'O', ' ', ' ', 'O'],
    ['O ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'O', ' '],
    ['O', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'O', ' ', ' ']
]

posicion_agente = [0, 0] 
ruta = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4)]
indice_ruta = 0

def imprimir_entorno():
    for i in range(len(definir_entorno)):
        for j in range(len(definir_entorno[i])):
            if [i, j] == posicion_agente:
                print('A', end=' ')
            else:
                print(definir_entorno[i][j], end=' ')
        print()
    print('\n')

def mover_agente():
    global indice_ruta
    if indice_ruta < len(ruta) - 1:
        nueva_posicion = list(ruta[indice_ruta + 1])
        if definir_entorno[nueva_posicion[0]][nueva_posicion[1]] == 'O':
            print("¡Obstáculo detectado! Cambiando dirección aleatoria.")
            indice_ruta = random.randint(0, len(ruta) - 1)
        else:
            indice_ruta += 1
            posicion_agente[0], posicion_agente[1] = nueva_posicion
    else:
        print("Ruta completa. Reiniciando...")
        indice_ruta = 0
        posicion_agente[0], posicion_agente[1] = ruta[indice_ruta]

while True:
    imprimir_entorno()
    mover_agente()
    time.sleep(1)
