def hola(nombre="Mundo"): 
    print ("Hola", nombre)

hola("Luis")
hola();

class animal:
    def __init__(self, patas=4, tipo="pequeño"):
        self.patas=patas
        self.tipo=tipo

class perro(animal):    
    def __init__(self, nombre="oddy", raza="jack"):
        self.nombre=nombre 
        self.raza=raza
        super
    #def saludo(self):
        #return "Te saluda %s" %self.nombre


perrito=perro(nombre="Rico", raza="ninguna")
perrito_juan=perro()
#print(perrito.tipo)
#print(perrito.patas)
print(perrito.nombre)
print(perrito.raza)

#perrito.saludo()
print(perrito_juan.nombre)
print(perrito_juan.raza)
#perrito_juan.saludo()