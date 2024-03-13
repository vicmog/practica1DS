from src.casaBuilder import CasaBuilder

class ChaletBuilder(CasaBuilder):

    def aniadir_cocina(self):
        self.casa.cocina = "Cocina para chalet"
    
    def aniadir_banio(self):
        self.casa.banio = "Baño para chalet"

    def aniadir_sala_de_estar(self):
        self.casa.sala_de_estar = "Sala de estar para chalet"
    
    def aniadir_dormitorio(self):
        self.casa.dormitorio = "Dormitorio para chalet"