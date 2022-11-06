from ast import main

class alumno():
    print("La clase alumno se ha creado con éxito.\n")

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "{} ha sacado un {}\n".format(self.nombre,self.nota)

    def calificacion(self):
        if self.nota>=5:
            print("Ha aprobado, ")
        
        else:
            print("Ha suspendido,")
    
def main():
    alumno1=alumno("Pedro",9)
    alumno1.calificacion()
    print(alumno1.__str__())

    alumno2=alumno("Pablo",3)
    alumno2.calificacion()
    print(alumno2.__str__())

    alumno3=alumno("Jaime",4.9)
    alumno3.calificacion()
    print(alumno3.__str__())

if __name__=="__main__":
    main()