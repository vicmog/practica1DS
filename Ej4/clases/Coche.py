from time import sleep

from clases.Motor import Motor
from ui.Controles import Controles
from ui.Salpicadero import Salpicadero


class Coche:
    def __init__(self):
        self.estado_motor = Motor().APAGADO
        self.revoluciones = 0
        self.velocidad = 0
        self.distancia_recorrida = 0

        self.controles = Controles(coche=self)
        self.salpicadero = Salpicadero(self.controles, nombre="Salpicadero", coche=self)
        # Asignamos la función de destruir la primera ventana cuando la segunda se elimina,
        # así conseguimos que se cierren ambas al mismo tiempo
        self.salpicadero.protocol("WM_DELETE_WINDOW", self.controles.destroy)

    def update(self):
        while True:
            print(self.revoluciones)
            if self.estado_motor == Motor().ACELERANDO:
                self.revoluciones += 100
                self.velocidad = self.revoluciones * 0.1
            elif self.estado_motor == Motor().FRENANDO:
                self.revoluciones -= 100
                self.velocidad = self.revoluciones * 0.1
            sleep(1)
