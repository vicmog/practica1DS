

from src.Cocina.CocinaBuilder import CocinaBuilder


class CocinaDeLujoBuilder(CocinaBuilder):

    def aniadir_horno(self):
        self.cocina.horno = "Horno de lujo"
    
    def aniadir_vitroceramica(self):
        self.cocina.vitroceramica = "Vitroceramica de lujo"
    
    def aniadir_lavavajillas(self):
        self.cocina.lavavajillas = "Lavavajillas de lujo"

    def aniadir_encimera(self):
        self.cocina.encimera = "Encimera de lujo"
