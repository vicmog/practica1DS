class Motor:
    def __init__(self):
        self.encendido = False
        self.acelerando = False

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def acelerar(self):
        self.acelerando = True

    def frenar(self):
        self.acelerando = False

    def is_encendido(self):
        return self.encendido
