from abc import ABC


class Bicicleta(ABC):

    def __init__(self, identificador, tipo):
        self.__identificador = identificador
        self.__tipo = tipo

    def get_identificador(self):
        return self.identificador
    
    def get_tipo(self):
        return self.tipo