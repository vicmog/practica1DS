from clases.Motor import Motor
from ui.Controles import Controles
from ui.Salpicadero import Salpicadero


class Coche:
    def __init__(self):
        self.estado_motor = Motor().APAGADO
        self.revoluciones = 0
        self.velocidad = 0
        self.distancia_recorrida = 0
        self.RADIO_RUEDA = 0.15
        print(self.revoluciones)

        self.controles = Controles(coche=self)
        self.salpicadero = Salpicadero(self.controles, nombre="Salpicadero", coche=self)
        # Asignamos la función de destruir la primera ventana cuando la segunda se elimina,
        # así conseguimos que se cierren ambas al mismo tiempo
        self.salpicadero.protocol("WM_DELETE_WINDOW", self.controles.destroy)
