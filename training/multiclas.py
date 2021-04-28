class Telefono: 
    def __init__(self, number):
        self.number = number
    def __init__(self):
        self.number = 5551525354
    

    ##EL metodo _repr_ es como la representacion oficial en cadena de la clase 
    def __repr__(self):
        return f'Telefono: {self.number}'
    
    def marcar(self):
        print('Marcando...')
    

class Camara: 
    def __init__(self):
        self.resolucion = '1020x900'
    
    def __repr__(self):
        return f'Resolucion: {self.resolucion}'

    def tomarFoto(self):
        print('Click!')
    
    def tomarVideo(self):
        print('Recording...')

class Calculadora:
    def __init__(self):
        self.data = [1,2,3]

    def __repr__(self):
        print(self.data)

    def calcular(self):
        print('calculando')

class smarthphone(Telefono, Camara, Calculadora):

    def __init__(self):
        Telefono.__init__(self)
        Camara.__init__(self)
        Calculadora.__init__(self)

    def __repr__(self):
        ##return f'{Telefono.__repr__(self)} {Camara.__repr__(self)} {Calculadora.__repr__(self)}'
        return f'{Telefono.__repr__(self)}'
    def __del_(self):
        print('Telefono apagado')


movil = smarthphone()
movil.marcar()
movil.tomarFoto()
movil.calcular()
print(movil.__repr__())