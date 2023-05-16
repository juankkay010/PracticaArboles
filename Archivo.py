class Archivo:
    def __init__(self, name):
        self.complete_name = name
        self.name = None
        self.extension = None
        self.peso = None
        self.madre = None
        self.separar_atributos()

    def separar_atributos(self):
        self.name, self.peso = self.complete_name.split()
        self.name, self.extension = self.name.split(".")

    def modificar_nombre(self, nombre):
        self.name = nombre

    def modificar_extension(self, extension):
        self.extension = extension

    def modificar_peso(self, peso):
        self.peso = peso

