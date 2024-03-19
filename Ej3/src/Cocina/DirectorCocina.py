class DirectorCocina:
    def __init__(self,builder):
        self.builder_cocina = builder
    
    def construir_cocina(self):
        self.builder_cocina.crear_cocina()
        self.builder_cocina.aniadir_horno()
        self.builder_cocina.aniadir_vitroceramica()
        self.builder_cocina.aniadir_lavavajillas()
        self.builder_cocina.aniadir_encimera()
        