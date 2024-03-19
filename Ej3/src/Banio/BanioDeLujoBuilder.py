

from src.Banio.BanioBuilder import BanioBuilder


class BanioDeLujoBuilder(BanioBuilder):
    def aniadir_ducha(self):
        self.banio.ducha = "Ducha de lujo"

    def aniadir_bidet(self):
        self.banio.bidet = "Bidet de lujo"

    def aniadir_lavabo(self):
        self.banio.lavabo = "Lavabo de lujo"

    def aniadir_espejo(self):
        self.banio.espejo = "Espejo de lujo"
        