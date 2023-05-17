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

    def calcular_peso(self):
        peso_total = 0
        if self.one is not None:
            if isinstance(self.one, Carpeta):
                peso_total += self.one.calcular_peso()
            else:
                peso_total += int(self.one.peso)
        if self.two is not None:
            if isinstance(self.two, Carpeta):
                peso_total += self.two.calcular_peso()
            else:
                peso_total += int(self.two.peso)
        if self.three is not None:
            if isinstance(self.three, Carpeta):
                peso_total += self.three.calcular_peso()
            else:
                peso_total += int(self.three.peso)
        if self.four is not None:
            if isinstance(self.four, Carpeta):
                peso_total += self.four.calcular_peso()
            else:
                peso_total += int(self.four.peso)
        return peso_total
