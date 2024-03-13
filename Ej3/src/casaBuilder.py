from abc import ABC, abstractmethod

from src.casa import Casa

class CasaBuilder(ABC):

    def __init__(self):
        self.casa = None

    def crear_casa(self):
        self.casa = Casa()
        
    @abstractmethod

    def aniadir_cocina(self):
        pass
        
    @abstractmethod

    def aniadir_banio(self):
        pass
        
    @abstractmethod

    def aniadir_sala_de_estar(self):
        pass
        
    @abstractmethod

    def aniadir_dormitorio(self):
        pass