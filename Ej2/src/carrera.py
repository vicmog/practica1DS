from abc import ABC


class Carrera(ABC):

    def __init__(self, tipo, bicicletas=[]):
        self.tipo = tipo
        self.bicicletas = bicicletas
        print("Se ha creado una carrera de tipo {self.tipo}")
