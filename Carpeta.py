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
            for i in [self.one, self.two, self.three, self.four]:     # Crea una lista con los hijos de la carpeta
                if isinstance(i, Carpeta) and isinstance(hijo, Carpeta):   # Verifica que Ambos sean de la clase Carpeta
                    if i.name == hijo.name:     # Si ambos nombres son iguales, no se puede agregar
                        return False
                if isinstance(i, Archivo) and isinstance(hijo, Archivo):   # Verifica que ambos sean de la clase Archivo
                    if i.name == hijo.name and i.extension == hijo.extension: # Si ambos nombres y extensiones son iguales, no se puede agregar
                        return False

            if self.one is None:
                self.one = hijo
            elif self.two is None:
                self.two = hijo       # Agrega el hijo al primer nodo disponible
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
