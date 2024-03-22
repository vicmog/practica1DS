from src.impl.bicicleta_montana import BicicletaMontana
from src.impl.carrera_montana import CarreraMontana
from src.factoria_carrera_bicicleta import FactoriaCarreraYBicicleta


class FactoriaMontana(FactoriaCarreraYBicicleta):
    def __init__(self):
        self.num_bicicletas = 0

    def crear_carrera(self):
        return CarreraMontana()

    def crear_bicicleta(self):
        identificador = self.num_bicicletas
        self.num_bicicletas += 1
        return BicicletaMontana(identificador=identificador)
