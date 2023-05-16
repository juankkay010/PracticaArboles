from Archivo import Archivo


class Carpeta:
    def __init__(self, name):
        self.name = name
        self.cantidad = 0
        self.madre = None
        self.one = None
        self.two = None
        self.three = None
        self.four = None

    def agregar_hijo(self, hijo):
        if self.cantidad < 4:
            for i in [self.one, self.two, self.three, self.four]:
                if isinstance(i, Carpeta) and isinstance(hijo, Carpeta):
                    if i.name == hijo.name:
                        return False
                if isinstance(i, Archivo) and isinstance(hijo, Archivo):
                    if i.name == hijo.name and i.extension == hijo.extension:
                        return False

            if self.one is None:
                self.one = hijo
            elif self.two is None:
                self.two = hijo
            elif self.three is None:
                self.three = hijo
            else:
                self.four = hijo
            hijo.madre = self
            self.cantidad += 1
            return True
        else:
            return False

    def modificar_nombre(self, nuevo_nombre):
        self.name = nuevo_nombre
