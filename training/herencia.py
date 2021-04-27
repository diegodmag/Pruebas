class infanteria:
    def __init__(self,nombre,armadura,arma):
        self.nombre = nombre 
        self.armadura = armadura
        self.arma = arma 
    
    def informacion(self):
        return 'Nombre: {}, Armadura: {}, Arma: {}'.format(self.nombre, self.armadura, self.arma)

#Aqui comenzamos con la herencia  
class piquero(infanteria):
    def falange(self, numero):
         return 'Una formacion utilizando {} en grupos de {}'.format(self.arma, numero)

class hombresDeArmas(infanteria):
    def carga(self, formacion):
         return 'Se realiza una carga usando {} en formacion {}'.format(self.arma, formacion)   


tercios = piquero('Tercios Espanoles', 'Coraza ligera', 'Pica')
rodelero = hombresDeArmas('Rodelero Espanol', 'Coraza pesada', 'Espada de Mano')

print(tercios.informacion())
print(rodelero.informacion())

print(tercios.falange(10))
print(rodelero.carga('Ala Imperial'))
