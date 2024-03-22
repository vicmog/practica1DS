from src.bicicleta import Bicicleta


class BicicletaMontana(Bicicleta):
    def __init__(self, identificador):
        super().__init__(tipo="Montaña", identificador=identificador)