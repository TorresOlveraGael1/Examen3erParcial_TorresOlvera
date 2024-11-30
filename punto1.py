#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la n property.

print(" ")
print("Torres Olvera Gael")
print(" ")


#Funcion inicial
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 6:
            return f"{self.nombre} ha aprobado con una nota de {self.nota}."
        else:
            return f"{self.nombre} no ha aprobado, su nota es {self.nota}."

#funcion para uso adecuado
def main():
    # Inicializar un objeto Alumno
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    nota_alumno = float(input("Ingrese la nota del alumno: "))
    
    alumno = Alumno(nombre_alumno, nota_alumno)
    
    #Imprimir datos del alumno
    alumno.imprimir_datos()
    
    #Mostrar resultado
    print(alumno.resultado())

if __name__ == "__main__":
    main()