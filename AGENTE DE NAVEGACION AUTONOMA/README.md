Este ejercicio implementa un agente de navegación autónoma que busca la ruta más corta en un laberinto utilizando el algoritmo de búsqueda en amplitud (BFS). El agente tiene como objetivo encontrar una ruta desde una posición de inicio hasta una meta, evitando las paredes y marcando el camino recorrido en el laberinto.

Estructura del Código
Clase Laberinto:
La clase Laberinto encapsula la lógica del laberinto y las operaciones relacionadas.
Atributos:
laberinto: Representación 2D del laberinto (matriz de caracteres).
inicio: Coordenadas de la posición inicial ('S').
meta: Coordenadas de la meta ('M').
filas y columnas: Tamaño del laberinto.
Métodos:
obtener_vecinos(nodo): Devuelve los vecinos adyacentes válidos de una celda, es decir, aquellas celdas libres (' ') donde el agente puede moverse.
buscar_ruta(): Implementa el algoritmo de búsqueda en amplitud (BFS) para encontrar la ruta más corta desde el inicio hasta la meta.
marcar_ruta(ruta): Marca las celdas por donde el agente ha pasado con la letra 'X', exceptuando las celdas de inicio ('S') y meta ('M').

Representación del Laberinto:
El laberinto es representado como una matriz de caracteres donde:
'S' es el punto de inicio.
'M' es la meta.
'#' representa las paredes.
' ' son los espacios libres por donde el agente puede moverse.
Flujo de Ejecución
Se define el laberinto, se especifican las posiciones de inicio y meta.
Se crea un objeto de la clase Laberinto con el laberinto, el inicio y la meta.
El método buscar_ruta() se utiliza para encontrar la ruta más corta. Si se encuentra un camino, se marca en el laberinto con 'X' y luego se imprime la matriz con el camino recorrido.

Salida:
Si se encuentra un camino, el programa imprime la ruta seguida por el agente como una lista de coordenadas.
