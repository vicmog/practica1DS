from filtros.CalcularVelocidad import CalcularVelocidad
from filtros.RepercutirRozamiento import RepercutirRozamiento
from filtros.CadenaFiltros import CadenaFiltros


class GestorFiltros:
    def __init__(self):
        self.cadena_filtros = CadenaFiltros()
        self.add_filtro(CalcularVelocidad(incremento_velocidad=100))
        self.add_filtro(RepercutirRozamiento(rozamiento=1))

    def add_filtro(self, filtro):
        self.cadena_filtros.addFiltro(filtro)

    def peticion_filtros(self, revoluciones, estado_motor):
        return self.cadena_filtros.ejecutar(
            revoluciones=revoluciones, estado_motor=estado_motor
        )
