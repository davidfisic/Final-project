# -*- coding: utf-8 -*-
"""
Created on Sun May 28 01:37:53 2023

@author: sebas
"""

import proyecto
import mov_recto

# Solicitar los valores al usuario
theta_deg = float(input("Ingrese el valor de theta (en grados): "))
x0 = float(input("Ingrese el valor de x0: "))
y0 = float(input("Ingrese el valor de y0: "))
v0 = float(input("Ingrese el valor de v0: "))
g = float(input("Ingrese el valor de g: "))

# Crear instancia de MovimientoParabolico
movimiento = proyecto.MovimientoParabolico(theta_deg, x0, y0, v0, g)

# Crear instancia de AnimacionMovimientoParabolico
animacion = proyecto.AnimacionMovimientoParabolico(movimiento)

# Mostrar la animación y el gráfico
animacion.mostrar_animacion()

# ejer_1 = mov_recto.MovimientoDim1()
# print(ejer_1.mensaje_cambio_posicion())
# print(ejer_1.mensaje_cambio_tiempo())
# print(ejer_1.v_prom())

# ejer_2 = mov_recto.VelocidadConstante()
# print(ejer_2.posicion_final())
# ejer_2.graficar_movimiento()