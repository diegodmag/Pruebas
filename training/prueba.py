class Mazzazzy:
    #En general todos los metodos reciben una referencia al objeto con self 
    
    #Metodo para inicializar el objeto, podria ser el constructor 
    def __init__(self,c,n,a):
        self.casta = c 
        self.nombre = n 
        self.arma = a 

    def _atacar_(self):
        print('El Mazzazzy '+ self.nombre + ' de la casta ' + self.casta + ' y con el arma '+ self.arma)

        #RETORNAR ATRIBUTO 
    def _imprimir_atributos_(self):
        #Al parecer el metodo getattr(x,y) regresa el atributo y de la clase x 
        print('La casta del Mazzazzi', getattr(self,'casta'))

        #VERIFICAR ATRIBUTO
    def _tiene_casta_(self):
        #Usamos la funcion hasattr para saber si la clase tiene un atributo 'casta'
        print('El individuo tiene casta?', hasattr(self,'casta'))


       #MODIFICAR ATRIBUTO  
    def _acender_a_guerrero_(self):
        #Vamos a utilizar la funcion setattr para modificar el VALOR de un atributo
        print(self.casta)
        setattr(self, 'casta', 'Guerrero')
        print('El individuo ', self.nombre, ' ha sido ancendido a Guerrero ')
        print(self.casta)
       #ELIMINAR ATRIBUTO 
    def _ejecutar_(self):
        #Utilizando delattr se elimina el atributo 
        print(self.nombre)
        delattr(self,'nombre')
        
maz = Mazzazzy('sith inferior', 'Vong', 'Vibroaxe')
maz2 = Mazzazzy('sith inferior', 'Vong', 'Vibroaxe')
#maz._atacar_()
#maz._imprimir_atributos_()
#maz._tiene_casta_()
#maz._acender_a_guerrero_()