import customtkinter


class Velocimetro(customtkinter.CTkFrame):
    def __init__(self, parent, coche):
        super().__init__(parent)
        self.coche = coche
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.label = customtkinter.CTkLabel(self, text="Velocidad")
        self.label.grid(row=0, column=0, sticky="ew", columnspan=2)
        self.velocidad = customtkinter.CTkLabel(
            self, text=str(self.coche.velocidad) + " km/h"
        )
        self.velocidad.grid(row=1, column=0, sticky="ew", columnspan=2)

    def update(self):
        self.velocidad.configure(text=str(self.coche.velocidad) + " km/h")
