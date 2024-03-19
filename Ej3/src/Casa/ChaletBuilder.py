from src.Casa.CasaBuilder import CasaBuilder
from src.Dormitorio import Dormitorio
from src.SalaDeEstar import SalaDeEstar

class ChaletBuilder(CasaBuilder):

    def aniadir_sala_de_estar(self):
        self.casa.sala_de_estar = SalaDeEstar(sala_de_estar="Sala de estar para chalet")
    
    def aniadir_dormitorio(self):
        self.casa.dormitorio = Dormitorio(dormitorio="Dormitorio para chalet")