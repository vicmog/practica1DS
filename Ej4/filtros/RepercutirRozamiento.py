from filtros.Filtro import Filtro


class RepercutirRozamiento(Filtro):
    def __init__(self, rozamiento):
        super().__init__()
        self.rozamiento = rozamiento

    def ejecutar(self, revoluciones, estado_motor) -> float:
        return max(0, revoluciones - self.rozamiento)
