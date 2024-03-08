from abc import ABC, abstractmethod
import random


class Carrera(ABC):

    def __init__(self, tipo, bicicletas=[]):
        self._tipo = tipo
        self._bicicletas = bicicletas

    def agregar_bicicleta(self, bicicleta):
        if bicicleta.get_tipo() == self._tipo:
            self._bicicletas.append(bicicleta)
            return True
        else:
            print (f'La bicicleta {bicicleta.get_identificador()} no es de tipo {self._tipo} si no de tipo {bicicleta.get_tipo()}')
            return False

    def _retirar_bicicleta_aleatoria(self):
        bicicleta = random.choice(self._bicicletas)
        self._bicicletas.remove(bicicleta)
        return bicicleta

    @abstractmethod
    def iniciar_carrera(self):
        pass