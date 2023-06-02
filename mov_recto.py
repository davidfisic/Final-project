# -*- coding: utf-8 -*-
"""
Created on Sun May 28 01:45:33 2023

@author: sebas
"""

import numpy as np
import matplotlib.pyplot as plt

class MovimientoDim1:
    """
    Clase que representa un movimiento unidimensional.

    Atributos:
    - x_f: posición final.
    - x_i: posición inicial.
    - t_f: tiempo final.
    - t_i: tiempo inicial.
    """

    def __init__(self):
        """
        Inicializa los atributos del movimiento.
        Solicita al usuario ingresar la posición final, posición inicial, tiempo final y tiempo inicial.
        """
        self.x_f = str(input("Ingrese la posición final en metros: "))
        self.x_i = eval(input("Ingrese la posición inicial en metros: "))
        self.t_f = eval(input("Ingrese el tiempo final en segundos: "))
        self.t_i = eval(input("Ingrese el tiempo inicial en segundos: "))

    def delta_x(self):
        """
        Calcula el cambio de posición.
        Retorna la diferencia entre la posición final y la posición inicial.
        """
        return float(self.x_f) - self.x_i

    def delta_t(self):
        """
        Calcula el cambio de tiempo.
        Retorna la diferencia entre el tiempo final y el tiempo inicial.
        """
        return self.t_f - self.t_i

    def v_prom(self):
        """
        Calcula la velocidad promedio.
        Divide el cambio de posición entre el cambio de tiempo.
        Retorna la velocidad promedio.
        """
        print("la velocidad promedio es {0} m/s".format(self.delta_x() / self.delta_t()))

    def mensaje_cambio_posicion(self):
        """
        Genera un mensaje con el cambio de posición.
        Retorna el mensaje formateado.
        """
        return "El cambio de posición es {0}".format(self.delta_x())

    def mensaje_cambio_tiempo(self):
        """
        Genera un mensaje con el cambio de tiempo.
        Retorna el mensaje formateado.
        """
        return "El cambio en el tiempo es {0}".format(self.delta_t())


class VelocidadConstante(MovimientoDim1):
    """
    Clase que representa un movimiento con velocidad constante.

    Atributos:
    - v: velocidad constante (atributo adicional a los de MovimientoDim1).
    """

    def __init__(self):
        """
        Inicializa los atributos del movimiento con velocidad constante.
        Solicita al usuario ingresar la velocidad.
        Llama al constructor de la clase padre (MovimientoDim1).
        Calcula la posición final utilizando la fórmula de posición final con velocidad constante.
        """
        self.v = eval(input("Ingrese la velocidad en m/s: "))
        super().__init__()
        if self.x_f == "":
            print("ok")
        self.x_f = self.x_i + self.v * self.delta_t()

    def posicion_final(self):
        """
        Genera un mensaje con la posición final.
        Retorna el mensaje formateado.
        """
        return "La posición final será: {0} m".format(self.x_f)

    def graficar_movimiento(self):
        """
        Grafica el movimiento con velocidad constante en función del tiempo.
        Utiliza la fórmula de posición con velocidad constante para generar los puntos del gráfico.
        Muestra el gráfico.
        """
        t = np.linspace(self.t_i, self.t_f, 100)
        x = self.x_i + self.v * (t - self.t_i)

        plt.plot(t, x)
        plt.xlabel('Tiempo')
        plt.ylabel('Posición')
        plt.title('Movimiento con velocidad constante')
        plt.grid(True)
        plt.show()

movimiento = VelocidadConstante()
movimiento.v_prom()
print(movimiento.posicion_final())
movimiento.graficar_movimiento()
