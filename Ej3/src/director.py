class Director:

    def __init__(self, builder):
        self._builder = builder

    def construir_casa(self):
        self._builder.crear_casa()
        self._builder.aniadir_cocina()
        self._builder.aniadir_banio()
        self._builder.aniadir_sala_de_estar()
        self._builder.aniadir_dormitorio()