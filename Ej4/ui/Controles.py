import customtkinter
from clases.Motor import Motor


class Controles(customtkinter.CTk):
    def __init__(self, nombre="Controles", motor=None):
        super().__init__()

        self.title(nombre)
        # self.geometry("500x150")
        self.grid_columnconfigure(3, weight=1)

        self.frameSuperior = customtkinter.CTkFrame(master=self, height=50)
        self.frameSuperior.grid(
            row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=3
        )
        self.estadoLabel = customtkinter.CTkLabel(self.frameSuperior, text="APAGADO")

        self.encenderButton = customtkinter.CTkButton(
            self, text="Encender", command=self.button_callback
        )
        self.encenderButton.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.acelerarButton = customtkinter.CTkButton(
            self, text="Acelerar", command=self.button_callback, state="disabled"
        )
        self.acelerarButton.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        self.frenarButton = customtkinter.CTkButton(
            self, text="Frenar", command=self.button_callback, state="disabled"
        )
        self.frenarButton.grid(row=1, column=2, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        print("button pressed")
