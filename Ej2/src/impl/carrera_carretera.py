from src.carrera import Carrera


class CarreraCarretera(Carrera):
    def __init__(self, bicicletas=[]):
        super().__init__(bicicletas=bicicletas, tipo='Carretera')
