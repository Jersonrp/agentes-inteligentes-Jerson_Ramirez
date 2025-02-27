from collections import deque

class Laberinto:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = meta
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])

    def obtener_vecinos(self, nodo):
        """Obtiene los vecinos adyacentes válidos del nodo"""
        x, y = nodo
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba
        vecinos = []

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.filas and 0 <= ny < self.columnas and self.laberinto[nx][ny] != '#':
                vecinos.append((nx, ny))

        return vecinos

    def buscar_ruta(self):
        """BFS para encontrar la ruta más corta"""
        queue = deque([(self.inicio, [self.inicio])])  # cola con el nodo inicial y su camino
        visitados = set()

        while queue:
            nodo_actual, camino = queue.popleft()

            if nodo_actual == self.meta:
                return camino  # Cuando se llega a la meta, devolver el camino

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                for vecino in self.obtener_vecinos(nodo_actual):
                    if vecino not in visitados:
                        queue.append((vecino, camino + [vecino]))  # Agregar nuevo camino

        return None  # Si no se encuentra un camino


# Definición del laberinto (5x5)
# 'S' = Inicio, 'M' = Meta, '#' = Pared, ' ' = Espacio libre
laberinto = [
    ['S', ' ', '#', ' ', ' '],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' '],
    [' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', 'M', '#']
]

# Posiciones de inicio y meta
inicio = (0, 0)  # 'S'
meta = (4, 3)    # 'M'

# Crear el objeto laberinto y buscar la ruta
agente = Laberinto(laberinto, inicio, meta)
camino = agente.buscar_ruta()

if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")