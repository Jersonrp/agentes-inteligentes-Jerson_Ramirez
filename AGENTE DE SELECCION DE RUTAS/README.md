En este ejercicio se implementa un agente que selecciona la mejor ruta en un entorno con múltiples caminos y valores de recompensa. El agente evalúa las diferentes rutas posibles y elige aquella con la mayor utilidad acumulada suma de las recompensas de las celdas en el camino.

Funcionalidad
Representación del Entorno:

El entorno se representa mediante una matriz de valores de recompensa donde cada celda tiene un valor que indica la recompensa al pasar por ella.
Las celdas con valores más altos representan caminos más beneficiosos para el agente.
Algoritmo de Búsqueda:

El agente utiliza un algoritmo de búsqueda en profundidad (DFS) para explorar todas las rutas desde el punto de inicio hasta el punto meta.
El agente acumula las recompensas de cada ruta visitada y selecciona el camino con la mayor utilidad (recompensa total).
Salida:

Una vez que el agente encuentra la meta, muestra la ruta óptima seleccionada junto con la utilidad total de esa ruta.
Clases y Métodos
Clase Agente: Representa al agente encargado de explorar el entorno.
Métodos principales:
obtener_vecinos(x, y): Obtiene las celdas adyacentes válidas desde las coordenadas (x, y).
calcular_utilidad(camino): Calcula la utilidad total de un camino sumando las recompensas de todas las celdas en ese camino.
buscar_ruta(): Utiliza un algoritmo de búsqueda en profundidad (DFS) para encontrar la ruta con la mayor utilidad.
