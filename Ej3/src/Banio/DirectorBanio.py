
class DirectorBanio:
    def __init__(self,builder):
        self.banio_builder = builder

    def construir_banio(self):
        self.banio_builder.crear_banio()
        self.banio_builder.aniadir_ducha()
        self.banio_builder.aniadir_bidet()
        self.banio_builder.aniadir_lavabo()
        self.banio_builder.aniadir_espejo()
        