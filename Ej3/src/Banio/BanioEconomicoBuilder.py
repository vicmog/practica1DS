
from src.Banio.BanioBuilder import BanioBuilder


class BanioEconomicoBuilder(BanioBuilder):
    
        def aniadir_ducha(self):
            self.banio.ducha = "Ducha economica"
    
        def aniadir_bidet(self):
            self.banio.bidet = "Bidet economica"
    
        def aniadir_lavabo(self):
            self.banio.lavabo = "Lavabo economica"
    
        def aniadir_espejo(self):
            self.banio.espejo = "Espejo economica"