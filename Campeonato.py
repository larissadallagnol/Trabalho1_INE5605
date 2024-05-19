# Entidade Campeonato

from Partida import Partida
from Equipe import Equipe

class Campeonato():
    def __init__(self, nome: str, equipes: list, partidas: list):
        self.__nome = nome
        self.__equipes = []
        self.__partidas = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def equipes(self):
        return self.__equipes
    
    @equipes.setter
    def equipes(self, equipes):
        self.__equipes = equipes
    
    @property
    def partidas(self):
        return self.__partidas
    
    @partidas.setter
    def partidas(self, partidas):
        self.__partidas = partidas
