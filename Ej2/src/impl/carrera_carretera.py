from src.carrera import Carrera


class CarreraCarretera(Carrera):
    def __init__(self, bicicletas=[]):
        super().__init__(bicicletas=bicicletas, tipo='Carretera')

    def iniciar_carrera(self):
        print('Iniciando carrera de carretera')
        
        for i in range(self.__bicicletas * 0.1):
            bicicleta = self.__retirar_bicicleta_aleatoria()
            print(f'La bicicleta {bicicleta.get_identificador()} ha terminado la carrera')