from src.Cocina.CocinaBuilder import CocinaBuilder


class CocinaEstandarBuilder(CocinaBuilder):

    def aniadir_horno(self):
        self.cocina.horno = "Horno estandar"

    def aniadir_vitroceramica(self):
        self.cocina.vitroceramica = "Vitroceramica estandar"

    def aniadir_lavavajillas(self):
        self.cocina.lavavajillas = "Lavavajillas estandar"
        
    def aniadir_encimera(self):
        self.cocina.encimera = "Encimera estandar"

