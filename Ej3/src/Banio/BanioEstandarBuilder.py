
from src.Banio.BanioBuilder import BanioBuilder


class BanioEstandarBuilder(BanioBuilder):

    def aniadir_ducha(self):
        self.banio.ducha = "Ducha estandar"

    def aniadir_bidet(self):
        self.banio.bidet = "Bidet estandar"

    def aniadir_lavabo(self):
        self.banio.lavabo = "Lavabo estandar"

    def aniadir_espejo(self):
        self.banio.espejo = "Espejo estandar"