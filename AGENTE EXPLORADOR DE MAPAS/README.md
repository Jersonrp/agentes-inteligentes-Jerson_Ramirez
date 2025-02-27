Este ejercicio implementa un agente explorador con estado interno que navega un entorno representado como una cuadrícula. El agente recuerda las áreas visitadas y evita repetir caminos ya explorados.

Funcionamiento

Definición del entorno: Se establece un mapa donde ' ' son espacios vacíos y 'O' son obstáculos.

Posición inicial: El agente comienza en la coordenada (0,0).

Direcciones posibles: El agente puede moverse en cuatro direcciones (derecha, abajo, izquierda, arriba).

Exploración del entorno:

Evalúa los movimientos válidos evitando obstáculos y lugares visitados.

Se mueve aleatoriamente a una celda permitida.

Si no hay movimientos disponibles, la exploración se detiene.

Bucle principal: Muestra el entorno y mueve al agente hasta que ya no haya opciones de movimiento.
