from ast import main

class Producto():
    print("El producto se ha creado con éxito")

    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo

    def __str__(self):
        return "El tipo de producto es {}, su nombre es {}, su precio es {} de euros y el codigo es {}\n".format(self.tipo, self.nombre, 
        self.precio, self.codigo)

def main():
    producto1=Producto(569381, "BMW M4 CSL", 119450, "Automóvil")
    print(producto1.__str__())
    producto2=Producto(884052, "Aston Martin Valkyrie", 2890000, "Automóvil")
    print(producto2.__str__())
    producto3=Producto(293604, "Mercedes AMG ONE", 2500000, "Automóvil")
    print(producto3.__str__())

if __name__=="__main__":
    main()
