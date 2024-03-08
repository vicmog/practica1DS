from abc import ABC, abstractmethod
import random


class Carrera(ABC):

    def __init__(self, tipo, bicicletas=[]):
        self.tipo = tipo
        self.bicicletas = bicicletas

    def agregar_bicicleta(self, bicicleta):
        if bicicleta.get_tipo == self.__tipo:
            self.bicicletas.append(bicicleta)
            return True
        else:
            print (f'La bicicleta {bicicleta.identificador} no es de tipo {self.__tipo}')
            return False

    def __retirar_bicicleta_aleatoria(self):
        bicicleta = random.choice(self.bicicletas)
        self.bicicletas.remove(bicicleta)
        return bicicleta

    @abstractmethod
    def iniciar_carrera(self):
        pass