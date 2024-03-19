from abc import ABC,abstractclassmethod

from src.Banio.Banio import Banio

class BanioBuilder(ABC):

    def __init__(self,banio=None):
        self.banio = banio
    
    def crear_banio(self):
        self.banio = Banio()

    @abstractclassmethod
    def aniadir_ducha(self):
        pass
    
    @abstractclassmethod
    def aniadir_bidet(self):
        pass

    @abstractclassmethod
    def aniadir_lavabo(self):
        pass

    @abstractclassmethod
    def aniadir_espejo(self):
        pass