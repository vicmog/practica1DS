from src.bicicleta import Bicicleta


class BicicletaCarretera(Bicicleta):
    def __init__(self, identificador):
        super().__init__(tipo="Carretera", identificador=identificador)