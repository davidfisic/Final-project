# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:36:04 2023

@author: sebas
"""

import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v_0, h_i, g):
        self.v_0 = v_0
        self.h_i = h_i
        self.g = g
    
    def calculate_distance(self):
        x_f = self.v_0 * ((2 * self.h_i / self.g) ** (1 / 2))
        return x_f
    
    def calculate_time(self):
        x_f = self.calculate_distance()
        t1 = x_f / self.v_0
        t2 = ((2 * self.h_i / self.g) ** (1 / 2))
        return t1, t2
    
    def calculate_height(self, t):
        h = (1 / 2) * self.g * t ** 2
        return h
    
    def plot_trajectory(self):
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
        
        # Mostrar la distancia final en la gráfica
        ax.annotate(f'Distancia final: {x_f:.2f} m', xy=(x_f, self.h_i - h[-1]),
                    xytext=(0, 0.05), 
                arrowprops=dict(facecolor='black', arrowstyle='->'))
        
        plt.show()

v_0 = float(input("Digite la velocidad inicial "))
h = float(input("Digite la altura "))
g = float(input("Digite la gravedad "))
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