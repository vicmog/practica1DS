from carrera import Carrera


class CarreraMontana(Carrera):
    def __init__(self, bicicletas=[]):
        super().__init__(bicicletas=bicicletas, tipo='Montaña')
