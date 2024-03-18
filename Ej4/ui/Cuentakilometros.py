import customtkinter


class Cuentakilometros(customtkinter.CTkFrame):
    def __init__(self, parent, coche):
        super().__init__(parent)
        self.coche = coche
        self.grid_columnconfigure((0, 1), weight=1)

        self.label = customtkinter.CTkLabel(self, text="Kilometros")
        self.label.grid(row=0, column=0, sticky="ew", columnspan=2)
        self.kilometros = customtkinter.CTkLabel(
            self, text=str(self.coche.distancia_recorrida) + " km"
        )
        self.kilometros.grid(row=1, column=0, sticky="ew", columnspan=2)
        self.sumar_kilometros()

    def sumar_kilometros(self):
        self.coche.distancia_recorrida += self.coche.velocidad / 3600
        self.after(1000, self.sumar_kilometros)

    def update(self):
        self.kilometros.configure(
            text="%.3f" % (self.coche.distancia_recorrida) + " km"
        )
