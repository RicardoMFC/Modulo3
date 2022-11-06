from ast import main

class alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("La clase alumno se ha creado con éxito.\n")

    def calificacion(self):
        if self.nota>=5:
            print("{} ha aprobado con un {}\n".format(self.nombre,self.nota))
        
        else:
            print("{} ha suspendido con un {}\n".format(self.nombre,self.nota))
            

        
def main():
    alumno1=alumno("Pablo",9)
    alumno1.calificacion
    


if __name__=="__main__":
    main()
