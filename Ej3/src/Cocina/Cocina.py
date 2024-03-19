class Cocina:

    def __init__(self,horno=None,vitroceramica=None,lavavajillas=None,encimera=None):
        self.horno = horno
        self.vitroceramica = vitroceramica
        self.lavavajillas = lavavajillas
        self.encimera = encimera 

    def __str__(self):
        return f"Horno: {self.horno} Vitroceramica: {self.vitroceramica} Lavavajillas: {self.lavavajillas} Encimera: {self.encimera}"
    