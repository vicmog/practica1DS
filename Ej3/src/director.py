class DirectorCasa:

    def __init__(self, builder):
        self.builder_casa = builder

    def construir_casa(self):
        self.builder_casa.crear_casa()
        self.builder_casa.aniadir_cocina()
        self.builder_casa.aniadir_banio()
        self.builder_casa.aniadir_sala_de_estar()
        self.builder_casa.aniadir_dormitorio()