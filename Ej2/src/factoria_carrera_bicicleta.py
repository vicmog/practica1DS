from abc import ABC, abstractmethod
from src.bicicleta import Bicicleta

from src.carrera import Carrera


class FactoriaCarreraYBicicleta(ABC):
    @abstractmethod
    def crear_carrera(self) -> Carrera: pass

    @abstractmethod
    def crear_bicicleta(self) -> Bicicleta: pass
