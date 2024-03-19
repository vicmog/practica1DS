from src.Cocina.CocinaBuilder import CocinaBuilder

class CocinaEconomicaBuilder(CocinaBuilder):
    def aniadir_horno(self):
        self.cocina.horno = "Horno economico"
    def aniadir_vitroceramica(self):
        self.cocina.vitroceramica = "Vitroceramica economica"
    def aniadir_lavavajillas(self):
        self.cocina.lavavajillas = "Lavavajillas economico"
    def aniadir_encimera(self):
        self.cocina.encimera = "Encimera economica"