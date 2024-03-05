from abc import ABC, abstractmethod
from bicicleta import Bicicleta

from carrera import Carrera


class FactoriaCarreraYBicicleta(ABC):
    @abstractmethod
    def crear_carrera(self) -> Carrera: pass

    @abstractmethod
    def crear_bicicleta(self) -> Bicicleta: pass
