from src.carrera import Carrera


class CarreraMontana(Carrera):
    def __init__(self, bicicletas=[]):
        super().__init__(bicicletas=bicicletas, tipo='Montaña')

    def iniciar_carrera(self):
        print(f'Iniciando carrera de {self._tipo} con {len(self._bicicletas)} bicicletas')
        
        for i in range(int(len(self._bicicletas) * 0.2)):
            bicicleta = self._retirar_bicicleta_aleatoria()
            print(f'La bicicleta {bicicleta.get_identificador()} ha abandonado la carrera de tipo {self._tipo}')