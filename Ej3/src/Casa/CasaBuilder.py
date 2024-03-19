from abc import ABC, abstractmethod

from src.Casa.Casa import Casa

class CasaBuilder(ABC):

    def __init__(self):
        self.casa = None

    def crear_casa(self):
        self.casa = Casa()
        

    def aniadir_cocina(self,cocina):
        self.casa.cocina = cocina
        

    def aniadir_banio(self,banio):
        self.casa.banio = banio
        
    @abstractmethod
    def aniadir_sala_de_estar(self):
        pass
        
    @abstractmethod
    def aniadir_dormitorio(self):
        pass