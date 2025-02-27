class Agente:
    def __init__(self, entorno, inicio, meta):
        self.entorno = entorno
        self.inicio = inicio
        self.meta = meta

    def obtener_vecinos(self, x, y):
        """Obtiene los vecinos adyacentes del nodo (x, y)"""
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        vecinos = []
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.entorno) and 0 <= ny < len(self.entorno[0]):
                vecinos.append((nx, ny))

        return vecinos

    def calcular_utilidad(self, camino):
        """Suma las recompensas de un camino"""
        return sum(self.entorno[x][y] for x, y in camino)

    def buscar_ruta(self):
        """Busca el camino con la mayor utilidad (búsqueda en profundidad)"""
        mejor_camino = []
        mejor_utilidad = float('-inf')  

        def dfs(x, y, camino):
            nonlocal mejor_camino, mejor_utilidad

           
            if (x, y) == self.meta:
                utilidad = self.calcular_utilidad(camino)
                if utilidad > mejor_utilidad:
                    mejor_utilidad = utilidad
                    mejor_camino = camino
                return

            for nx, ny in self.obtener_vecinos(x, y):
                if (nx, ny) not in camino:  
                    dfs(nx, ny, camino + [(nx, ny)])

   
        dfs(self.inicio[0], self.inicio[1], [self.inicio])

        return mejor_camino, mejor_utilidad



entorno = [
    [1, -1, 2, 0, 1],
    [2,  1, -1, 3, 0],
    [0,  2,  1, -1, 2],
    [1,  3,  2, 1, -1],
    [0, 1, 0,  2, 3]
]

inicio = (0, 0)
meta = (4, 4)


agente = Agente(entorno, inicio, meta)
camino, utilidad = agente.buscar_ruta()

if camino:
    print("Camino óptimo:", camino)
    print("Utilidad total:", utilidad)
else:
    print("No se encontró un camino.")
