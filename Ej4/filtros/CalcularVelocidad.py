from filtros.Filtro import Filtro
from clases.Motor import Motor


class CalcularVelocidad(Filtro):
    def __init__(self, incremento_velocidad):
        super().__init__()
        self.incremento_velocidad = incremento_velocidad

    def ejecutar(self, revoluciones, estado_motor) -> float:
        if estado_motor == Motor.ACELERANDO:
            return min(5000, revoluciones + self.incremento_velocidad)
        elif estado_motor == Motor.FRENANDO:
            return min(5000, revoluciones - self.incremento_velocidad)
        return min(revoluciones, 5000)
