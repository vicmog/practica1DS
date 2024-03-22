from filtros.Filtro import Filtro


class CadenaFiltros:
    def __init__(self):
        self.filtros = []

    def addFiltro(self, filtro):
        if not (isinstance(filtro, Filtro)):
            raise Exception("Se ha intentado agregar un objeto que no es un filtro")
        self.filtros.append(filtro)

    def ejecutar(self, revoluciones, estado_motor) -> float:
        revoluciones_finales = revoluciones
        for filtro in self.filtros:
            revoluciones_finales = filtro.ejecutar(
                revoluciones=revoluciones_finales, estado_motor=estado_motor
            )
        return revoluciones_finales
