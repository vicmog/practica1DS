from src.factoria_montana import FactoriaMontana
from src.factoria_carretera import FactoriaCarretera


def main():
    factoria_montana = FactoriaMontana()
    carrera_montana = factoria_montana.crear_carrera()
    for i in range(10):
        carrera_montana.agregar_bicicleta(bicicleta=factoria_montana.crear_bicicleta())
    carrera_montana.iniciar_carrera()

    factoria_carretera = FactoriaCarretera()
    carrera_carretera = factoria_carretera.crear_carrera()
    for i in range(10):
        carrera_carretera.agregar_bicicleta(bicicleta=factoria_carretera.crear_bicicleta())
    carrera_carretera.iniciar_carrera()


if __name__ == "__main__":
    main()
