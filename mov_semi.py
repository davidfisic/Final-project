# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:36:04 2023

@author: sebas
"""

import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    """
    Clase que representa un proyectil en movimiento parabólico.

    Atributos:
        v_0 (float): Velocidad inicial del proyectil en m/s.
        h_i (float): Altura inicial desde la cual se lanza el proyectil en metros.
        g (float): Aceleración debido a la gravedad en m/s^2.
    """

    def __init__(self, v_0, h_i, g):
        """
        Inicializa una instancia de la clase Projectile.

        Args:
            v_0 (float): Velocidad inicial del proyectil en m/s.
            h_i (float): Altura inicial desde la cual se lanza el proyectil en metros.
            g (float): Aceleración debido a la gravedad en m/s^2.
        """
        self.v_0 = v_0
        self.h_i = h_i
        self.g = g

    def calculate_distance(self):
        """
        Calcula la distancia horizontal recorrida por el proyectil.

        Returns:
            float: Distancia horizontal recorrida por el proyectil en metros.
        """
        x_f = self.v_0 * ((2 * self.h_i / self.g) ** (1 / 2))
        return x_f

    def calculate_time(self):
        """
        Calcula el tiempo total de vuelo del proyectil.

        Returns:
            float: Tiempo total de vuelo del proyectil en segundos.
        """
        x_f = self.calculate_distance()
        t1 = x_f / self.v_0
        t2 = ((2 * self.h_i / self.g) ** (1 / 2))
        return t1, t2

    def calculate_height(self, t):
        """
        Calcula la altura del proyectil en un instante de tiempo dado.

        Args:
            t (float): Instante de tiempo en segundos.

        Returns:
            float: Altura del proyectil en metros en el instante de tiempo dado.
        """
        h = (1 / 2) * self.g * t ** 2
        return h

    def plot_trajectory(self):
        """
        Grafica la trayectoria del proyectil.
        """
        t1, t2 = self.calculate_time()
        t = np.linspace(0, t2, 100)
        x = self.v_0 * t
        h = self.calculate_height(t)

        fig, ax = plt.subplots()
        ax.plot(x, self.h_i - h, label='Trayectoria')
        ax.plot(x, np.zeros_like(x), '--', color='gray', label='Tierra')
        ax.set_xlim(0, self.calculate_distance())
        ax.set_ylim(0, self.h_i)
        ax.set_xlabel('Distancia horizontal (m)')
        ax.set_ylabel('Altura (m)')
        ax.set_title('Trayectoria del proyectil')
        ax.legend()
        plt.grid(True)

        plt.show()


def error_altura():
    """
    Solicita al usuario que ingrese la altura inicial del proyectil.

    Returns:
        float: Altura inicial del proyectil en metros.
    """
    while True:
        try:
            h = float(input("Digite la altura en metros: "))
            return h
        except ValueError:
            print("La altura debe ser un número.")

def error_gravedad():
    """
    Solicita al usuario que ingrese la aceleración debido a la gravedad.

    Returns:
        float: Aceleración debido a la gravedad en m/s^2.
    """
    while True:
        try:
            g = float(input("Digite la gravedad: "))
            if g == 0:
                print("Error: La gravedad no puede ser cero.")
            else:
                return g
        except ValueError:
            print("La gravedad es un valor en unidades de m/s^2.")

def error_v_0():
    """
    Solicita al usuario que ingrese la velocidad inicial del proyectil.

    Returns:
        float: Velocidad inicial del proyectil en m/s.
    """
    while True:
        try:
            v_0 = float(input("Digite la velocidad inicial en m/s: "))
            return v_0
        except ValueError:
            print("La velocidad debe ser un número en m/s.")


# Solicitar al usuario los valores necesarios
g = error_gravedad()
h = error_altura()
v_0 = error_v_0()

# Crear una instancia de la clase Projectile
projectile = Projectile(v_0, h, g)

# Calcular y mostrar la distancia final
x_f = projectile.calculate_distance()
print("Distancia final:", x_f)

# Calcular y mostrar los tiempos
t1, t2 = projectile.calculate_time()
print("Tiempo total:", t1)

# Graficar la trayectoria
projectile.plot_trajectory()
