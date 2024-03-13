from src.casaBuilder import CasaBuilder

class ApartamentoBuilder(CasaBuilder):
    
    def aniadir_cocina(self):
        self.casa.cocina = "Cocina para apartamento"
    
    def aniadir_banio(self):
        self.casa.banio = "Baño para apartamento"

    def aniadir_sala_de_estar(self):
        self.casa.sala_de_estar = "Sala de estar para apartamento"
    
    def aniadir_dormitorio(self):
        self.casa.dormitorio = "Dormitorio para apartamento"