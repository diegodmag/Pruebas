class Calculadora:
    def __init__(self, number):
        self.number = number
        self.data = [0 for i in range(number)]
    
    def ingresadato(self):
        self.data = [int(input('Ingresa el dato' + str(i+1)+ '=')) for i in self.data]      

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    
    def suma(self):
        a,b = self.data
        s = a + b 
        return s

    def resta(self):
        a,b = self.data
        r = a - b 
        return r
    
    def producto(self):
        a,b = self.data
        p = a * b 
        return p
    
    def division(self):
        a,b = self.data
        d = a / b 
        return d

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    
    def cuadrada(self):
        import math
        a = self.data 
        return math.sqrt(a)

op_1 = op_basicas()

#Algunas funciones utiles en la herencia 

print(isinstance(op_1,op_basicas))

print(issubclass(op_basicas,Calculadora))

print(issubclass(raiz,Calculadora))