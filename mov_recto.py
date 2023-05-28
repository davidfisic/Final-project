# -*- coding: utf-8 -*-
"""
Created on Sun May 28 01:45:33 2023

@author: sebas
"""

import numpy as np
import matplotlib.pyplot as plt

class MovimientoDim1:
    def __init__(self):
        self.x_f = str(input("Ingrese la posición final: "))
        self.x_i = eval(input("Ingrese la posición inicial: "))
        self.t_f = eval(input("Ingrese el tiempo final: "))
        self.t_i = eval(input("Ingrese el tiempo inicial: "))
        
    def delta_x(self):
        return float(self.x_f) - self.x_i
    
    def delta_t(self):
        return self.t_f - self.t_i
        
    def v_prom(self):
        return self.delta_x() / self.delta_t()
    
    def mensaje_cambio_posicion(self):
        return "El cambio de posición es {0}".format(self.delta_x())
    
    def mensaje_cambio_tiempo(self):
        return "El cambio en el tiempo es {0}".format(self.delta_t())

class VelocidadConstante(MovimientoDim1):
    def __init__(self):
        self.v = eval(input("Ingrese la velocidad: "))
        super().__init__()
        if self.x_f == "":
            print("ok")
        self.x_f = self.x_i + self.v * self.delta_t()
    
    def posicion_final(self):
        return "La posición final será: {0}".format(self.x_f)
    
    def graficar_movimiento(self):
        t = np.linspace(self.t_i, self.t_f, 100)
        x = self.x_i + self.v * (t - self.t_i)
        
        plt.plot(t, x)
        plt.xlabel('Tiempo')
        plt.ylabel('Posición')
        plt.title('Movimiento con velocidad constante')
        plt.grid(True)
        plt.show()


