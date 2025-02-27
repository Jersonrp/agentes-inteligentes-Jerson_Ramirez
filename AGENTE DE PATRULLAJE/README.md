Este programa implementa un agente reflejo que patrulla una ruta predefinida en un entorno con obstáculos.

Funcionamiento: El agente sigue una serie de coordenadas especificadas en la variable ruta. Si encuentra un obstáculo ('O'), cambia su dirección de manera aleatoria. Al completar la ruta, vuelve a iniciarla desde el principio.

Estructura del Código
definir_entorno: Matriz que representa el entorno donde el agente se mueve. Los obstáculos están representados por 'O' y '0'.
posicion_agente: Coordenadas actuales del agente.
ruta: Lista de posiciones que el agente debe recorrer.
indice_ruta: Índice que indica la posición actual del agente en la ruta.
Funciones
imprimir_entorno():
Muestra la matriz en la consola, con el agente representado por 'A'.
mover_agente():
Mueve al agente a la siguiente posición de la ruta.
Si encuentra un obstáculo, cambia su dirección aleatoriamente dentro de la ruta.
Si llega al final de la ruta, reinicia desde el inicio.
Ejecución
El programa se ejecuta en un bucle infinito donde se imprimen los movimientos del agente en la consola con una pausa de 1 segundo entre cada paso.
