from math import pi
import customtkinter

from ui.Velocimetro import Velocimetro
from ui.Cuentarevoluciones import Cuentarevoluciones
from ui.Cuentakilometros import Cuentakilometros
from filtros.GestorFiltros import GestorFiltros


class Salpicadero(customtkinter.CTkToplevel):
    def __init__(self, parent, coche, nombre="Salpicadero"):
        super().__init__(parent)
        self.geometry("400x300")
        self.coche = coche
        self.velocimetro = Velocimetro(self, coche)
        self.cuentarevoluciones = Cuentarevoluciones(self, coche)
        self.cuentakilometros = Cuentakilometros(self, coche)

        self.title(nombre)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.velocimetro.grid(
            row=0, column=0, ipadx=20, padx=20, pady=20, sticky="ew", columnspan=3
        )

        self.cuentarevoluciones.grid(
            row=1, column=0, ipadx=20, padx=20, pady=20, sticky="ew", columnspan=3
        )

        self.cuentakilometros.grid(
            row=2, column=0, ipadx=20, padx=20, pady=20, sticky="ew", columnspan=3
        )

        self.gestor_filtros = GestorFiltros()

        self.update()

    def update(self):
        self.coche.revoluciones = self.gestor_filtros.peticion_filtros(
            revoluciones=self.coche.revoluciones, estado_motor=self.coche.estado_motor
        )
        self.coche.velocidad = (
            2 * pi * self.coche.revoluciones * self.coche.RADIO_RUEDA * (60 / 1000)
        )
        self.velocimetro.update()
        self.cuentarevoluciones.update()
        self.cuentakilometros.update()
        self.after(500, self.update)
