# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:34:07 2023

@author: sebas
"""

class Resistor:
    """
    la clase Resistor tiene un atributo resistance que representa su 
    resistencia en ohmios. También tiene dos métodos: calculate_current y 
    calculate_voltage. calculate_current toma un voltaje como argumento y 
    devuelve la corriente que fluye a través del resistor según la ley de Ohm. 
    calculate_voltage, por otro lado, toma una corriente como argumento y 
    devuelve el voltaje a través del resistor.
    """
    def __init__(self, resistance):
        self.resistance = resistance

    def calculate_current(self, voltage):
        return voltage / self.resistance

    def calculate_voltage(self, current):
        return current * self.resistance
    
"""
En este ejemplo, se crea un resistor con una resistencia de 100 ohmios y se 
aplica un voltaje de 5 voltios. Se calcula la corriente a través del resistor 
utilizando el método calculate_current y se imprime en pantalla. Luego se 
establece una corriente de 0.05 amperios y se calcula el voltaje a través del 
resistor utilizando el método calculate_voltage, que también se imprime en 
pantalla.
"""
resistor = Resistor(100)  # crea un resistor de 100 ohmios
voltage = 5  # voltaje aplicado al resistor
current = resistor.calculate_current(voltage)  # calcula la corriente a través del resistor
print("La corriente a través del resistor es:", current, "amperios")

current = 0.05  # corriente que fluye a través del resistor
voltage = resistor.calculate_voltage(current)  # calcula el voltaje a través del resistor
print("El voltaje a través del resistor es:", voltage, "voltios")

print("-"*50)

"""
"""

class Resistor:
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
class Circuit:
    def __init__(self, resistors):
        self.resistors = resistors
    
    def get_resistance_series(self):
        total_resistance = 0
        for resistor in self.resistors:
            total_resistance += resistor.get_value()
        return total_resistance
    
    def get_resistance_parallel(self):
        total_resistance = 0
        for resistor in self.resistors:
            total_resistance += 1/resistor.get_value()
        return 1/total_resistance
    
r1 = Resistor(10)
r2 = Resistor(20)
r3 = Resistor(30)

circuit = Circuit([r1, r2, r3])
series_resistance = circuit.get_resistance_series()
parallel_resistance = circuit.get_resistance_parallel()

print("Resistencia en serie:", series_resistance)
print("Resistencia en paralelo:", parallel_resistance)

print("-"*50)

"""
"""


"""
resistencia en serie 
"""

Req=0

n = int(input("cantidad de resistencias: "))

for x in range (1,n+1):
    R=float(input("R? "))
    Req=Req+R
    print(Req)
print("Resistencia equivalente= ",Req)

print("-"*50)

"""
Resistencias en paralelo
"""
Rt=0

n = int(input("cantidad de resistencias: "))

for x in range (1,n+1):
    R=float(input("R? "))
    Rt=Rt+(1/R)
Req=1/Rt
print("Resistencia equivalente= ",Req)

print("-"*50)