import customtkinter
from clases.Motor import Motor


class Controles(customtkinter.CTk):
    def __init__(self, coche, nombre="Controles"):
        super().__init__()

        self.title(nombre)
        self.coche = coche
        # self.geometry("500x150")
        self.grid_columnconfigure(3, weight=1)

        self.frameSuperior = customtkinter.CTkFrame(master=self, height=50)
        self.frameSuperior.grid(
            row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=3
        )
        self.frameSuperior.grid_columnconfigure(0, weight=1)
        self.estadoLabel = customtkinter.CTkLabel(
            self.frameSuperior, text="APAGADO", anchor="center"
        )
        self.estadoLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.encenderButton = customtkinter.CTkButton(
            self, text="Encender", command=self.encender_apagar_motor
        )
        self.encenderButton.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.acelerarButton = customtkinter.CTkButton(
            self, text="Acelerar", command=self.acelerar, state="disabled"
        )
        self.acelerarButton.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        self.frenarButton = customtkinter.CTkButton(
            self, text="Frenar", command=self.frenar, state="disabled"
        )
        self.frenarButton.grid(row=1, column=2, padx=20, pady=20, sticky="ew")
        self.update()

    def encender_apagar_motor(self):
        if self.coche.estado_motor == Motor().APAGADO:
            self.coche.estado_motor = Motor().ENCENDIDO
        else:
            self.coche.estado_motor = Motor().APAGADO

    def acelerar(self):
        if (
            self.coche.estado_motor == Motor().ENCENDIDO
            or self.coche.estado_motor == Motor().FRENANDO
        ):
            self.coche.estado_motor = Motor().ACELERANDO
        elif self.coche.estado_motor == Motor().ACELERANDO:
            self.coche.estado_motor = Motor().ENCENDIDO

    def frenar(self):
        if (
            self.coche.estado_motor == Motor().ENCENDIDO
            or self.coche.estado_motor == Motor().ACELERANDO
        ):
            self.coche.estado_motor = Motor().FRENANDO
        elif self.coche.estado_motor == Motor().FRENANDO:
            self.coche.estado_motor = Motor().ENCENDIDO

    def update(self):
        if self.coche.estado_motor == Motor().ENCENDIDO:
            self.estadoLabel.configure(text="ENCENDIDO")
            self.acelerarButton.configure(text="Acelerar", text_color="white")
            self.frenarButton.configure(text="Frenar", text_color="white")
        elif self.coche.estado_motor == Motor().APAGADO:
            self.estadoLabel.configure(text="APAGADO")
            self.acelerarButton.configure(text="Acelerar", text_color="white")
            self.frenarButton.configure(text="Frenar", text_color="white")
        elif self.coche.estado_motor == Motor().FRENANDO:
            self.estadoLabel.configure(text="FRENANDO")
            self.acelerarButton.configure(text="Acelerar", text_color="white")
            self.frenarButton.configure(text="Soltar freno", text_color="red")
        elif self.coche.estado_motor == Motor().ACELERANDO:
            self.estadoLabel.configure(text="ACELERANDO")
            self.acelerarButton.configure(text="Soltar acelerador", text_color="red")
            self.frenarButton.configure(text="Frenar", text_color="white")

        if self.coche.estado_motor == Motor().ENCENDIDO:
            self.encenderButton.configure(text="Apagar")
            self.acelerarButton.configure(state="normal")
            self.frenarButton.configure(state="normal")
        elif self.coche.estado_motor == Motor().APAGADO:
            self.encenderButton.configure(text="Encender")
            self.acelerarButton.configure(state="disabled")
            self.frenarButton.configure(state="disabled")
        elif self.coche.estado_motor == Motor().FRENANDO:
            self.estadoLabel.configure(text="FRENANDO")
        elif self.coche.estado_motor == Motor().ACELERANDO:
            self.estadoLabel.configure(text="ACELERANDO")

        self.after(100, self.update)
