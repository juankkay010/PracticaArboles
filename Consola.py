import sys

from QuaternaryTree import QuaternaryTree


class Sistema:
    def __init__(self):
        self.tree = QuaternaryTree()
        self.opciones = {
            "1": self.agregar_carpeta,
            "2": self.agregar_archivo,
            "3": self.modificar_carpeta,
            "4": self.modificar_archivo,
            "5": self.salir
        }

    def mostrar_menu(self):
        print("""
                    \n
                    ===================================
                    Menú de opciones:\n
                    1. Agregar Carpeta
                    2. Agregar Archivo
                    3. Modificar Carpeta
                    4. Modificar Archivo
                    5. Salir
                    ===================================
                    """)

    def agregar_carpeta(self):
        nombre_carpeta_nueva = input("Ingrese el nombre de la carpeta: ")
        nombre_carpeta_madre = input("Ingrese el nombre de la carpeta madre: ")
        if self.tree.agregar_carpeta(nombre_carpeta_nueva, nombre_carpeta_madre):
            print("La carpeta fue agregada correctamente")
        else:
            print("No se pudo agregar la carpeta")

    def agregar_archivo(self):
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        nombre_carpeta_madre = input("Ingrese el nombre de la carpeta madre: ")
        if self.tree.agregar_archivo(nombre_archivo, nombre_carpeta_madre):
            print("El archivo fue agregado correctamente")
        else:
            print("El archivo no se puedo agregar")

    def modificar_carpeta(self):
        nombre_viejo = input("Ingrese el nombre de la carpeta a cambiar: ")
        nombre_nuevo = input("Ingrese el nuevo nombre de la carpeta: ")
        if self.tree.modificar_carpeta(nombre_viejo, nombre_nuevo):
            print("La carpeta ha cambiado de nombre")
        else:
            print("La carpeta no se ha podido modificar")

    def modificar_archivo(self):
        nombre_viejo = input("Ingrese el nombre de el archivo a cambiar: ")
        nombre_nuevo = input("Ingrese el nuevo nombre de el archivo (Si es necesario): ")
        peso = input("Ingrese el nuevo peso de el archivo (Si es necesario): ")
        extension = input("Ingrese la nueva extension de el archivo (Si es necesario): ")
        if self.tree.modificar_archivo(nombre_viejo, nombre_nuevo, extension, peso):
            print("El archivo se ma modificado correctamente")
        else:
            print("El archivo no se ha podido modificar")

    def ejecutar(self):
        while True:
            self.tree.imprimir_arbol()
            self.mostrar_menu()
            opcion = input("Seleccione una opcion: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                accion()
            else:
                print("Opcion Incorrecta")

    def salir(self):
        sys.exit(0)


if __name__ == "__main__":
    sistema = Sistema()
    sistema.ejecutar()
