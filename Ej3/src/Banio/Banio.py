
class Banio:

    def __init__(self,ducha=None,bidet=None,lavabo=None,espejo=None):
        self.ducha = ducha
        self.bidet = bidet
        self.lavabo = lavabo
        self.espejo = espejo
    
    def __str__(self):
        return f"Ducha: {self.ducha} Bidet: {self.bidet} Lavabo: {self.lavabo} Espejo: {self.espejo}"
