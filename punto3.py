#Desarrollar un programa que cargue los datos de un triángulo.

print(" ")
print("Torres Olvera Gael")
print(" ")

#Función inicial
class Metodos:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mostrar_datos(self):
        print(f"Primer lado: {self.lado1}")
        print(f"Segundo lado: {self.lado2}")
        print(f"Tercer lado: {self.lado3}")

    def triangulo_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "El triángulo es Equilátero"
        return None

    def triangulo_isosceles(self):
        if (self.lado1 == self.lado2 and self.lado1 != self.lado3) or \
        (self.lado1 == self.lado3 and self.lado2 != self.lado3) or \
        (self.lado2 == self.lado3 and self.lado1 != self.lado2):
            return "El triángulo es Isósceles"
        return None

    def triangulo_escaleno(self):
        if self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
            return "El triángulo es Escaleno"
        return None

#Solicitar datos
def main():
    lado1 = float(input("Ingrese cuánto mide el primer lado del triángulo: "))
    lado2 = float(input("Ingrese cuánto mide el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese cuánto mide el tercer lado del triángulo: "))

    #Crear una instancia de la clase Metodos
    triangulo = Metodos(lado1, lado2, lado3)

    #Mostrar los datos del triángulo
    triangulo.mostrar_datos()

    #Determinar el tipo de triángulo
    tipo_equilatero = triangulo.triangulo_equilatero()
    tipo_isosceles = triangulo.triangulo_isosceles()
    tipo_escaleno = triangulo.triangulo_escaleno()

    #Imprimir el tipo de triángulo
    if tipo_equilatero:
        print(tipo_equilatero)
    elif tipo_isosceles:
        print(tipo_isosceles)
    elif tipo_escaleno:
        print(tipo_escaleno)
    else:
        print("Los lados no forman un triángulo válido.")

if __name__ == "__main__":
    main()