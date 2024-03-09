from abc import ABC


class Bicicleta(ABC):

    def __init__(self, identificador, tipo):
        self._identificador = identificador
        self._tipo = tipo

    def get_identificador(self):
        return self._identificador

    def get_tipo(self):
        return self._tipo

    def duplicar(self):
        return Bicicleta(self._identificador, self._tipo)
