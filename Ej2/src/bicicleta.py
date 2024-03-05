from abc import ABC


class Bicicleta(ABC):

    def __init__(self, identificador, tipo):
        self.identificador = identificador
        self.tipo = tipo
