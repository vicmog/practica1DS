import customtkinter

from ui.Velocimetro import Velocimetro


class Salpicadero(customtkinter.CTkToplevel):
    def __init__(self, parent, coche, nombre="Salpicadero"):
        super().__init__(parent)
        self.pressed = False
        self.coche = coche
        self.velocimetro = Velocimetro(self, coche)

        self.title(nombre)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.velocimetro.grid(row=3, column=0,ipadx=20, padx=20, pady=20, sticky="ew", columnspan=3)
        self.button = customtkinter.CTkButton(
            self, text="my button", command=self.button_callback
        )
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 20),
            sticky="w",
            columnspan=2,
        )
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=0, column=1, padx=20, pady=(0, 20), sticky="w")

    def button_callback(self):
        print("button pressed")
        print(self.coche.estado_motor)
        if self.pressed:
            self.button.configure(
                text="my button", fg_color="#1e90ff", hover_color="#6ec6ff"
            )
            self.pressed = False
        else:
            self.button.configure(
                text="button pressed", fg_color="#f73123", hover_color="#fc766d"
            )
            self.pressed = True
        print(self.checkbox_1.get())
