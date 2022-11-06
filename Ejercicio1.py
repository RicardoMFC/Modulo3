from ast import main

class alumno():        
    print("La clase alumno se ha creado con éxito.\n")

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def calificacion(self):
        if self.nota>=5:
            print("{} ha aprobado con un {}\n".format(self.nombre,self.nota))
        
        else:
            print("{} ha suspendido con un {}\n".format(self.nombre,self.nota))

def main():
    alumno1=alumno("Pedro",9)
    alumno1.calificacion()
    alumno2=alumno("Pablo",3)
    alumno2.calificacion()
    alumno3=alumno("Jaime",4.9)
    alumno3.calificacion()

if __name__=="__main__":
    main()
