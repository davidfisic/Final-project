# Movimiento Parabólico y Movimiento con Velocidad Constante

Este proyecto consiste en una implementación en Python de dos tipos de movimiento: el movimiento parabólico y el movimiento con velocidad constante. El objetivo es calcular y graficar las trayectorias de estos movimientos y proporcionar información relevante sobre ellos.

## Movimiento Parabólico

El movimiento parabólico representa el movimiento de un objeto lanzado en un ángulo y velocidad determinados. El objeto sigue una trayectoria parabólica y se ve afectado por la gravedad. La clase `MovimientoParabolico` implementa los cálculos y propiedades relacionadas con este tipo de movimiento.

### Clase `MovimientoParabolico`

Esta clase tiene los siguientes atributos:

- `theta`: ángulo de lanzamiento en grados.
- `v0`: velocidad inicial en metros por segundo.
- `g`: aceleración debido a la gravedad (valor por defecto: 9.8 m/s^2).
- `x0`: posición inicial en el eje x (valor por defecto: 0).
- `y0`: posición inicial en el eje y (valor por defecto: 0).

Y los siguientes métodos:

- `x_pos(t)`: calcula la posición en el eje x en un tiempo dado.
- `y_pos(t)`: calcula la posición en el eje y en un tiempo dado.
- `t_max()`: calcula el tiempo en el cual la altura máxima es alcanzada.
- `y_max()`: calcula la altura máxima alcanzada.
- `x_medio()`: calcula la posición en el eje x en el tiempo medio del vuelo.
- `x_max()`: calcula la posición máxima en el eje x alcanzada durante el vuelo.

### Clase `AnimacionMovimientoParabolico`

Esta clase se encarga de generar una animación que muestra la trayectoria del movimiento parabólico.

Tiene los siguientes atributos:

- `movimiento_parabolico`: instancia de la clase `MovimientoParabolico`.
- `t`: arreglo de tiempos para los cuales se calculan las posiciones.
- `x`: arreglo de posiciones en el eje x correspondientes a los tiempos.
- `y`: arreglo de posiciones en el eje y correspondientes a los tiempos.
- `N`: número de puntos en la animación.
- `fig`, `ax`, `ln`: objetos de matplotlib para crear y mostrar la animación.

Y los siguientes métodos:

- `actualizar(i)`: función que se ejecuta en cada frame de la animación para actualizar la posición del objeto.
- `mostrar_animacion()`: muestra la animación completa del movimiento parabólico.

## Movimiento con Velocidad Constante

El movimiento con velocidad constante representa el movimiento de un objeto que se desplaza a una velocidad constante en línea recta. La clase `VelocidadConstante` implementa los cálculos y funciones relacionadas con este tipo de movimiento.

### Clase `MovimientoDim1`

Esta clase es una clase base que representa un movimiento unidimensional. Tiene los siguientes atributos y métodos:

- `x_f`: posición final.
- `x_i`: posición inicial.
- `t_f`: tiempo final.
- `t_i`: tiempo inicial.
- `delta_x()`: calcula el cambio de posición.
- `delta_t()`: calcula el cambio de tiempo.
- `v_prom()`: calcula la velocidad promedio.
- `mensaje_cambio_posicion()`: muestra un mensaje con el cambio de posición.
- `mensaje_cambio_tiempo()`: muestra un mensaje con el cambio de tiempo.

### Clase `VelocidadConstante`

Esta clase hereda de `MovimientoDim1` y representa un movimiento con velocidad constante. Además de los atributos y métodos de la clase padre, tiene los siguientes atributos y métodos adicionales:

- `v`: velocidad constante.
- `posicion_final()`: muestra un mensaje con la posición final.
- `graficar_movimiento()`: grafica el movimiento en función del tiempo.

## Cómo utilizar el programa

1. Ejecuta el programa y sigue las instrucciones que se te presenten.
2. Para el movimiento parabólico, ingresa el ángulo de lanzamiento y la velocidad inicial.
3. Se mostrará una animación con la trayectoria del movimiento y los valores de altura máxima y posición máxima en el eje x.
4. Para el movimiento con velocidad constante, ingresa la posición inicial, posición final, tiempo inicial, tiempo final y velocidad.
5. Se mostrará la posición final calculada y se graficará el movimiento en función del tiempo.

## Requisitos del entorno

- Python 3.x
- Bibliotecas de Python: `numpy`, `matplotlib`

por Sebastian Rivera 
