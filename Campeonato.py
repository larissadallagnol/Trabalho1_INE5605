# Entidade Campeonato

from Partida import Partida
from Equipe import Equipe

class Campeonato():
    def __init__(self, nome_campeonato: str, equipes_campeonato: list):
        self.__nome_campeonato = nome_campeonato
        self.__equipes_campeonato = []
        self.__partidas_campeonato = []

    @property
    def nome_campeonato(self):
        return self.__nome_campeonato
    
    @nome_campeonato.setter
    def nome_campeonato(self, nome_campeonato):
        self.__nome_campeonato = nome_campeonato
    
    @property
    def equipes_campeonato(self):
        return self.__equipes_campeonato
    
    @equipes_campeonato.setter
    def equipes_campeonato(self, equipes_campeonato):
        self.__equipes_campeonato = equipes_campeonato

    '''def adicionar_equipe_campeonato(self, equipe: Equipe):
        if isinstance(equipe, Equipe):
            existe_equipe = False
            for equipes in self.__equipes_campeonato:
                if equipes == equipe:
                    existe_equipe = True
            if existe_equipe is False:
                self.__equipes_campeonato.append(equipe)
        return

    def adicionar_partida_campeonato(self, partida: Partida):
        return'''