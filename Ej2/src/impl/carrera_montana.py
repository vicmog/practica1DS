from src.carrera import Carrera
import random


class CarreraMontana(Carrera):
    def __init__(self, bicicletas=[]):
        super().__init__(bicicletas=bicicletas, tipo='Montaña')

    def iniciar_carrera(self):
        print(f'Iniciando carrera de {self._tipo} con {len(self._bicicletas)} bicicletas')
        num_bicicletas = len(self._bicicletas)

        for i in range(int(num_bicicletas * 0.2 * 2)):
            bicicleta = self._retirar_bicicleta_aleatoria()
            print(f'La bicicleta {bicicleta.get_identificador()} ha abandonado la carrera de tipo {self._tipo}')

        for i in range(int(num_bicicletas * 0.2)):
            bicicleta = random.choice(self._bicicletas_retiradas).duplicar()
            self.agregar_bicicleta(bicicleta)
            print(f'¡La bicicleta {bicicleta.get_identificador()} ha vuelto a la carrera de tipo {self._tipo} con otro ciclista!')

        print(f'La carrera de tipo {self._tipo} ha terminado con {len(self._bicicletas)} bicicletas')
