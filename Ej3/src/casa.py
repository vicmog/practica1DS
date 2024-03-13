class Casa():

    def __init__(self):
        self.cocina = None
        self.banio = None
        self.sala_de_estar = None
        self.dormitorio = None

    def __str__(self):
        return f"Casa:\nCocina:{ self.cocina }\nBaño:{self.banio}\nSala de estar:{self.sala_de_estar}\nDormitorio:{self.dormitorio}"
