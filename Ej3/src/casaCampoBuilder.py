from src.casaBuilder import CasaBuilder

class CasaCampoBuilder(CasaBuilder):
    
    def aniadir_cocina(self):
        self.casa.cocina = "Cocina para casa de campo"
    
    def aniadir_banio(self):
        self.casa.banio = "Baño para casa de campo"

    def aniadir_sala_de_estar(self):
        self.casa.sala_de_estar = "Sala de estar para casa de campo"
    
    def aniadir_dormitorio(self):
        self.casa.dormitorio = "Dormitorio para casa de campo"