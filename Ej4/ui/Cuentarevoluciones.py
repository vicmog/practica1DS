import customtkinter


class Cuentarevoluciones(customtkinter.CTkFrame):
    def __init__(self, parent, coche):
        super().__init__(parent)
        self.coche = coche
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.label = customtkinter.CTkLabel(self, text="Revoluciones")
        self.label.grid(row=0, column=0, sticky="ew", columnspan=2)
        self.revoluciones = customtkinter.CTkLabel(
            self, text=str(self.coche.revoluciones) + " rpm"
        )
        self.revoluciones.grid(row=1, column=0, sticky="ew", columnspan=2)
