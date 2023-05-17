from Archivo import Archivo
from Carpeta import Carpeta


class QuaternaryTree:
    def __init__(self):
        self.carpeta_raiz = Carpeta("Carpeta Raiz")

    def agregar_carpeta(self, nombre_carpeta_nueva, nombre_carpeta_madre):
        carpeta_madre = self.buscar_carpeta(nombre_carpeta_madre, self.carpeta_raiz)
        if carpeta_madre is not None and isinstance(carpeta_madre, Carpeta):
            nueva_carpeta = Carpeta(nombre_carpeta_nueva)
            carpeta_madre.agregar_hijo(nueva_carpeta)
            return True
        else:
            return False

    def agregar_archivo(self, nombre_archivo, nombre_carpeta_madre):
        carpeta_madre = self.buscar_carpeta(nombre_carpeta_madre, self.carpeta_raiz)
        if carpeta_madre is not None and isinstance(carpeta_madre, Carpeta):
            nuevo_archivo = Archivo(nombre_archivo)
            carpeta_madre.agregar_hijo(nuevo_archivo)
            return True
        else:
            return False

    def buscar_carpeta(self, nombre, carpeta_inicial):
        if nombre == self.carpeta_raiz.name:
            return self.carpeta_raiz
        if isinstance(carpeta_inicial, Carpeta):
            if nombre == carpeta_inicial.name:
                return carpeta_inicial
        if isinstance(carpeta_inicial, Archivo):
            if nombre == carpeta_inicial.complete_name:
                return carpeta_inicial
        if isinstance(carpeta_inicial, Carpeta):
            if carpeta_inicial.one is not None:
                resultado = self.buscar_carpeta(nombre, carpeta_inicial.one)
                if resultado is not None:
                    return resultado
            if carpeta_inicial.two is not None:
                resultado = self.buscar_carpeta(nombre, carpeta_inicial.two)
                if resultado is not None:
                    return resultado
            if carpeta_inicial.three is not None:
                resultado = self.buscar_carpeta(nombre, carpeta_inicial.three)
                if resultado is not None:
                    return resultado
            if carpeta_inicial.four is not None:
                resultado = self.buscar_carpeta(nombre, carpeta_inicial.four)
                if resultado is not None:
                    return resultado
        return None

    def modificar_carpeta(self, nombre_viejo, nombre_nuevo):
        carpeta_actual = self.buscar_carpeta(nombre_viejo, self.carpeta_raiz)
        carpeta_madre = carpeta_actual.madre
        for i in [carpeta_madre.one, carpeta_madre.two, carpeta_madre.three, carpeta_madre.four]:
            if i and i.name == nombre_nuevo:
                return False

        if carpeta_actual:
            carpeta_actual.modificar_nombre(nombre_nuevo)
            return True
        else:
            return False

    def buscar_archivo(self, nombre_archivo, nodo_actual):
        if isinstance(nodo_actual, Archivo):
            if nodo_actual.name == nombre_archivo:
                return nodo_actual
        elif isinstance(nodo_actual, Carpeta):
            if nodo_actual.one is not None:
                resultado = self.buscar_archivo(nombre_archivo, nodo_actual.one)
                if resultado is not None:
                    return resultado
            if nodo_actual.two is not None:
                resultado = self.buscar_archivo(nombre_archivo, nodo_actual.two)
                if resultado is not None:
                    return resultado
            if nodo_actual.three is not None:
                resultado = self.buscar_archivo(nombre_archivo, nodo_actual.three)
                if resultado is not None:
                    return resultado
            if nodo_actual.four is not None:
                resultado = self.buscar_archivo(nombre_archivo, nodo_actual.four)
                if resultado is not None:
                    return resultado
        return None

    def modificar_archivo(self, nombre_viejo, nombre_nuevo=None, extension=None, peso=None):
        archivo = self.buscar_archivo(nombre_viejo, self.carpeta_raiz)
        if archivo:
            carpeta_madre = archivo.madre
            for i in [carpeta_madre.one, carpeta_madre.two, carpeta_madre.three, carpeta_madre.four]:
                if isinstance(i, Archivo):
                    if i and i.name == nombre_nuevo and i.extension == extension:
                        return False

        if nombre_nuevo:
            archivo.modificar_nombre(nombre_nuevo)
        if extension:
            archivo.modificar_extension(extension)
        if peso:
            archivo.modificar_peso(peso)

    def imprimir_arbol(self):
        self.imprimir_subarbol(self.carpeta_raiz, 0)

    def imprimir_subarbol(self, nodo_actual, nivel):
        print(" " * nivel, end="")
        if isinstance(nodo_actual, Archivo):
            print("+ " + nodo_actual.name + "." + nodo_actual.extension + " " + nodo_actual.peso)
        if isinstance(nodo_actual, Carpeta):
            print("- " + nodo_actual.name)
            if nodo_actual.one is not None:
                self.imprimir_subarbol(nodo_actual.one, nivel + 2)
            if nodo_actual.two is not None:
                self.imprimir_subarbol(nodo_actual.two, nivel + 2)
            if nodo_actual.three is not None:
                self.imprimir_subarbol(nodo_actual.three, nivel + 2)
            if nodo_actual.four is not None:
                self.imprimir_subarbol(nodo_actual.four, nivel + 2)

    def retornar_carpeta_mas_pesada(self, carpeta):
        carpeta_pesada = carpeta
        peso_maximo = 0
        if isinstance(carpeta, Carpeta):
            if carpeta.one is not None and isinstance(carpeta.one, Carpeta):
                peso = carpeta.one.calcular_peso()
                carpeta_actual = self.retornar_carpeta_mas_pesada(carpeta.one)
                if peso > peso_maximo:
                    carpeta_pesada = carpeta_actual
                    peso_maximo = peso
            if carpeta.two is not None and isinstance(carpeta.two, Carpeta):
                peso = carpeta.two.calcular_peso()
                carpeta_actual = self.retornar_carpeta_mas_pesada(carpeta.two)
                if peso > peso_maximo:
                    carpeta_pesada = carpeta_actual
                    peso_maximo = peso
            if carpeta.three is not None and isinstance(carpeta.three, Carpeta):
                peso = carpeta.three.calcular_peso()
                carpeta_actual = self.retornar_carpeta_mas_pesada(carpeta.three)
                if peso > peso_maximo:
                    carpeta_pesada = carpeta_actual
                    peso_maximo = peso
            if carpeta.four is not None and isinstance(carpeta.four, Carpeta):
                peso = carpeta.four.calcular_peso()
                carpeta_actual = self.retornar_carpeta_mas_pesada(carpeta.four)
                if peso > peso_maximo:
                    carpeta_pesada = carpeta_actual
                    peso_maximo = peso
        return carpeta_pesada

    def buscar_ruta(self, nombre):
        return self._buscar_ruta(nombre, self.carpeta_raiz, "")

    def _buscar_ruta(self, nombre, nodo_actual, ruta_actual):
        if isinstance(nodo_actual, Carpeta) and nodo_actual.name == nombre:
            return ruta_actual + "/" + nombre + "/"
        if isinstance(nodo_actual, Archivo) and nodo_actual.name == nombre:
            return ruta_actual + "/" + nodo_actual.name + "." + nodo_actual.extension
        if isinstance(nodo_actual, Carpeta):
            if nodo_actual.one is not None:
                ruta = self._buscar_ruta(nombre, nodo_actual.one, ruta_actual + "/" + nodo_actual.name)
                if ruta is not None:
                    return ruta
            if nodo_actual.two is not None:
                ruta = self._buscar_ruta(nombre, nodo_actual.two, ruta_actual + "/" + nodo_actual.name)
                if ruta is not None:
                    return ruta
            if nodo_actual.three is not None:
                ruta = self._buscar_ruta(nombre, nodo_actual.three, ruta_actual + "/" + nodo_actual.name)
                if ruta is not None:
                    return ruta
            if nodo_actual.four is not None:
                ruta = self._buscar_ruta(nombre, nodo_actual.four, ruta_actual + "/" + nodo_actual.name)
                if ruta is not None:
                    return ruta
        return None


arbol = QuaternaryTree()
arbol.agregar_carpeta("Carpeta 1", "Carpeta Raiz")
arbol.agregar_carpeta("Carpeta 2", "Carpeta 1")
arbol.agregar_archivo("aqui.json 32", "Carpeta 1")
arbol.agregar_archivo("hola.jpg 128", "Carpeta 1")
arbol.agregar_archivo("hola.jpg 64", "Carpeta 2")
arbol.agregar_archivo("hola.csv 1024", "Carpeta 1")
print(arbol.retornar_carpeta_mas_pesada(arbol.carpeta_raiz).name)
arbol.imprimir_arbol()
