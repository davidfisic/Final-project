import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class MovimientoParabolico:
    """
    Clase que representa el movimiento parabólico de un proyectil.

    Atributos:
        theta (float): Ángulo de lanzamiento en grados.
        v0 (float): Velocidad inicial del proyectil en m/s.
        g (float): Aceleración debido a la gravedad en m/s^2. (Valor por defecto: 9.8)
        x0 (float): Posición inicial en el eje x. (Valor por defecto: 0)
        y0 (float): Posición inicial en el eje y. (Valor por defecto: 0)
    """

    def __init__(self, theta, v0, g=9.8, x0=0, y0=0):
        """
        Inicializa una instancia de la clase MovimientoParabolico.

        Args:
            theta (float): Ángulo de lanzamiento en grados.
            v0 (float): Velocidad inicial del proyectil en m/s.
            g (float, opcional): Aceleración debido a la gravedad en m/s^2. (Valor por defecto: 9.8)
            x0 (float, opcional): Posición inicial en el eje x. (Valor por defecto: 0)
            y0 (float, opcional): Posición inicial en el eje y. (Valor por defecto: 0)
        """
        self.theta = np.deg2rad(theta)  # Convertir el ángulo de grados a radianes
        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        self.g = g

    def x_pos(self, t):
        """
        Calcula la posición en el eje x en un instante de tiempo dado.

        Args:
            t (float): Instante de tiempo en segundos.

        Returns:
            float: Posición en el eje x en el instante de tiempo dado.
        """
        return self.x0 + self.v0 * np.cos(self.theta) * t

    def y_pos(self, t):
        """
        Calcula la posición en el eje y en un instante de tiempo dado.

        Args:
            t (float): Instante de tiempo en segundos.

        Returns:
            float: Posición en el eje y en el instante de tiempo dado.
        """
        return self.y0 + (self.v0 * np.sin(self.theta) * t) - ((self.g * t**2) / 2)

    def t_max(self):
        """
        Calcula el tiempo máximo de vuelo del proyectil.

        Returns:
            float: Tiempo máximo de vuelo en segundos.
        """
        v0_y = self.v0 * np.sin(self.theta)
        return v0_y / self.g

    def y_max(self):
        """
        Calcula la altura máxima alcanzada por el proyectil.

        Returns:
            float: Altura máxima alcanzada en metros.
        """
        t = self.t_max()
        return self.y0 + (self.v0 * np.sin(self.theta) * t) - ((self.g * t**2) / 2)

    def x_medio(self):
        """
        Calcula la posición en el eje x en el tiempo medio de vuelo.

        Returns:
            float: Posición en el eje x en el tiempo medio de vuelo en metros.
        """
        t = self.t_max()
        return self.x0 + self.v0 * np.cos(self.theta) * t

    def x_max(self):
        """
        Calcula la distancia máxima alcanzada por el proyectil.

        Returns:
            float: Distancia máxima alcanzada en metros.
        """
        t = 2 * self.t_max()
        return self.x0 + self.v0 * np.cos(self.theta) * t


class AnimacionMovimientoParabolico:
    """
    Clase que crea una animación del movimiento parabólico de un proyectil.

    Atributos:
        movimiento_parabolico (MovimientoParabolico): Instancia de la clase MovimientoParabolico.
        t (numpy.ndarray): Array de tiempo.
        x (numpy.ndarray): Array de posiciones en el eje x.
        y (numpy.ndarray): Array de posiciones en el eje y.
        N (int): Número de frames de la animación.
        fig (matplotlib.figure.Figure): Figura de la animación.
        ax (matplotlib.axes.Axes): Ejes de la animación.
        ln (matplotlib.lines.Line2D): Línea de la animación.
    """

    def __init__(self, movimiento_parabolico):
        """
        Inicializa una instancia de la clase AnimacionMovimientoParabolico.

        Args:
            movimiento_parabolico (MovimientoParabolico): Instancia de la clase MovimientoParabolico.
        """
        self.movimiento_parabolico = movimiento_parabolico
        self.t = np.linspace(0, 2 * movimiento_parabolico.t_max(), 100)
        self.x = movimiento_parabolico.x_pos(self.t)
        self.y = movimiento_parabolico.y_pos(self.t)
        self.N = len(self.t)
        self.fig, self.ax = plt.subplots()
        self.ln, = plt.plot(self.x, self.y, 'ro')

    def actualizar(self, i):
        """
        Actualiza la posición del proyectil en la animación para un frame dado.

        Args:
            i (int): Índice del frame.

        Returns:
            matplotlib.lines.Line2D: Línea actualizada de la animación.
        """
        self.ln.set_data(self.x[i], self.y[i])
        return self.ln

    def mostrar_animacion(self):
        """
        Muestra la animación del movimiento parabólico del proyectil.
        """
        self.ax.set_xlim(-1, self.movimiento_parabolico.x_max() + 10)
        self.ax.set_ylim(-1, self.movimiento_parabolico.y_max() + 10)
        self.ax.set_xlabel('posición en x')
        self.ax.set_ylabel('posición en y')
        self.ax.set_title("Movimiento parabólico")
        plt.plot(self.x, self.y)

        ani = animation.FuncAnimation(self.fig, self.actualizar, range(self.N),
                                      interval=0.00001)
        plt.scatter(self.movimiento_parabolico.x_medio(),
                    self.movimiento_parabolico.y_max(), marker="o")
        plt.scatter(self.movimiento_parabolico.x_max(), 0, marker="o")
        self.ax.annotate('y_max', xy=(self.movimiento_parabolico.x_medio(),
                                      self.movimiento_parabolico.y_max()),
                         xytext=(self.movimiento_parabolico.x_medio() + 5,
                                 self.movimiento_parabolico.y_max() + 5),
                         arrowprops=dict(facecolor='darkblue', arrowstyle='->'))
        self.ax.annotate('x_max', xy=(self.movimiento_parabolico.x_max(), 0),
                         xytext=(self.movimiento_parabolico.x_max(), 20),
                         arrowprops=dict(facecolor='darkblue', arrowstyle='->'))
        plt.grid()
        plt.show()

def error():
    while True:
        try:
            # Pedir al usuario que ingrese el ángulo y la velocidad inicial
            theta = float(input("Ingrese el ángulo en grados (°): "))
            v0 = float(input("Ingrese la velocidad inicial en (m/s): "))
            
            # Crear una instancia de MovimientoParabolico con los valores ingresados
            movimiento_parabolico = MovimientoParabolico(theta, v0)
            
            # Crear una instancia de AnimacionMovimientoParabolico y mostrar la animación
            animacion = AnimacionMovimientoParabolico(movimiento_parabolico)
            animacion.mostrar_animacion()

            # Imprimir los valores de y_max y x_max
            print(f"y_max: {movimiento_parabolico.y_max()}")
            print(f"x_max: {movimiento_parabolico.x_max()}")

            break  # Salir del bucle si se ingresaron números válidos

        except ValueError:
            print("Error: Las entradas deben ser números. Inténtelo nuevamente.")

error()