from abc import ABC, abstractmethod

from src.Cocina.Cocina import Cocina

class CocinaBuilder(ABC):
    def __init__(self,cocina=None):
        self.cocina = cocina
    
    def crear_cocina(self):
        self.cocina = Cocina()
    
    @abstractmethod
    def aniadir_horno(self):
        pass

    @abstractmethod
    def aniadir_vitroceramica(self):
        pass

    @abstractmethod
    def aniadir_lavavajillas(self):
        pass

    @abstractmethod
    def aniadir_encimera(self):
        pass



