class Dormitorio:
    def __init__(self,dormitorio=None):
        self.dormitorio = dormitorio
    
    def __str__(self):
        return f"Dormitorio: {self.dormitorio}"