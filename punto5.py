#Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

print(" ")
print("Torres Olvera Gael")
print(" ")

#Clase de contacto
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

#Funcion principal
class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto añadido exitosamente.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado:")
                print(contacto)
                return
        print("Contacto no encontrado.")

#Funcion para editar el contacto
    def editar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
                nuevo_telefono = input("Ingrese el nuevo teléfono (deje en blanco para no cambiar): ")
                nuevo_email = input("Ingrese el nuevo email (deje en blanco para no cambiar): ")
                
                if nuevo_nombre:
                    contacto.nombre = nuevo_nombre
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                if nuevo_email:
                    contacto.email = nuevo_email
                
                print("Contacto editado exitosamente.")
                return
        print("Contacto no encontrado.")

    #Menu para escoger
    def menu(self):
        while True:
            print("\n--- Menú de la Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Cerrando agenda...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")


#Código para ejecutar la agenda
if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()