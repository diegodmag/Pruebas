    class Trooper: 
    #Constructor 
    def __init__(self,nombre,clase,batallon):
        self.nombre = nombre
        self.clase = clase 
        self.batallon = batallon
    
    #Obtener informacion 
    def informacion(self):
        return 'Nombre: {} Clase: {} Batallon: {}'.format(self.nombre, self.clase, self.batallon)


tp_1 = Trooper('Hopkins','Death-Trooper',401)
tp_2 = Trooper('Jonson','Ark-Trooper',705)