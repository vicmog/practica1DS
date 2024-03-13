from src.director import Director
from src.chaletBuilder import ChaletBuilder
from src.apartamentoBuilder import ApartamentoBuilder
from src.casaCampoBuilder import CasaCampoBuilder

def main():
    casa_chalet = ChaletBuilder()
    director = Director(casa_chalet)
    director.construir_casa()
    print(casa_chalet.casa)

    casa_apartamento = ApartamentoBuilder()
    director2 = Director(casa_apartamento)
    director2.construir_casa()
    print(casa_apartamento.casa)

    casa_casaCampo = CasaCampoBuilder()
    director3 = Director(casa_casaCampo)
    director3.construir_casa()
    print(casa_casaCampo.casa)

if __name__ == "__main__":
    main()