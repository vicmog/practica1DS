import customtkinter

from ui.Velocimetro import Velocimetro
from ui.Cuentarevoluciones import Cuentarevoluciones
from ui.Cuentakilometros import Cuentakilometros


class Salpicadero(customtkinter.CTkToplevel):
    def __init__(self, parent, coche, nombre="Salpicadero"):
        super().__init__(parent)
        self.pressed = False
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
        self.update()

    def update(self):
        self.velocimetro.update()
        self.cuentarevoluciones.update()
        self.cuentakilometros.update()
        self.after(100, self.update)
