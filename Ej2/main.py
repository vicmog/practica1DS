from src.factoria_montana import FactoriaMontana


def main():
    factoria_montana = FactoriaMontana()
    bicicletas = []
    bicicletas.append(factoria_montana.crear_bicicleta())
    bicicletas.append(factoria_montana.crear_bicicleta())
    bicicletas.append(factoria_montana.crear_bicicleta())

    for bicicleta in bicicletas:
        print(bicicleta.identificador)


if __name__ == "__main__":
    main()
