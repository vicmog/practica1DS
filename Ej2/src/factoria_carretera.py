from src.impl.bicicleta_carretera import BicicletaCarretera
from src.impl.carrera_carretera import CarreraCarretera


class FactoriaCarretera:
    def __init__(self):
        self.num_bicicletas = 0

    def crear_carrera(self):
        return CarreraCarretera()

    def crear_bicicleta(self):
        identificador = self.num_bicicletas
        self.num_bicicletas += 1
        return BicicletaCarretera(identificador=identificador)
