

from src.Banio.BanioDeLujoBuilder import BanioDeLujoBuilder
from src.Banio.BanioEconomicoBuilder import BanioEconomicoBuilder
from src.Banio.BanioEstandarBuilder import BanioEstandarBuilder
from src.Banio.DirectorBanio import DirectorBanio
from src.Casa.ApartamentoBuilder import ApartamentoBuilder
from src.Casa.CasaCampoBuilder import CasaCampoBuilder
from src.Casa.ChaletBuilder import ChaletBuilder
from src.Casa.DirectorCasa import DirectorCasa
from src.Cocina.CocinaDeLujoBuilder import CocinaDeLujoBuilder
from src.Cocina.CocinaEconomicaBuilder import CocinaEconomicaBuilder
from src.Cocina.CocinaEstandarBuilder import CocinaEstandarBuilder



def main():
    casa_chalet = ChaletBuilder()
    director = DirectorCasa(casa_chalet,CocinaDeLujoBuilder(),BanioEstandarBuilder())
    director.construir_casa()
    print(casa_chalet.casa)

    casa_apartamento = ApartamentoBuilder()
    director2 = DirectorCasa(casa_apartamento,CocinaEstandarBuilder(),BanioEconomicoBuilder())
    director2.construir_casa()
    print(casa_apartamento.casa)

    casa_casaCampo = CasaCampoBuilder()
    director3 = DirectorCasa(casa_casaCampo,CocinaEconomicaBuilder(),BanioDeLujoBuilder())
    director3.construir_casa()
    print(casa_casaCampo.casa)

if __name__ == "__main__":
    main()