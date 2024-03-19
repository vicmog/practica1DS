from src.Banio.BanioDeLujoBuilder import BanioDeLujoBuilder
from src.Banio.DirectorBanio import DirectorBanio
from src.Cocina.DirectorCocina import DirectorCocina


class DirectorCasa:

    def __init__(self, builderCasa,builderCocina,builderBanio):
        self.builder_casa = builderCasa
        self.directorCocina = DirectorCocina(builderCocina)
        self.directorBanio = DirectorBanio(builderBanio)
    

    def construir_casa(self):
        self.builder_casa.crear_casa()

        self.directorCocina.construir_cocina()
        self.builder_casa.aniadir_cocina(cocina=self.directorCocina.builder_cocina.cocina)

        self.directorBanio.construir_banio()
        self.builder_casa.aniadir_banio(banio=self.directorBanio.banio_builder.banio)


        self.builder_casa.aniadir_sala_de_estar()
        self.builder_casa.aniadir_dormitorio()