# Entidade Campeonato

class Campeonato():
    def __init__(self, nome: str, equipes: list, partidas: list):
        self.__nome = nome
        self.__equipes = []
        self.__partidas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def equipes(self):
        return self.__equipes

    @property
    def partidas(self):
        return self.__partidas
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @equipes.setter
    def equipes(self, equipes):
        self.__equipes = equipes
    
    @partidas.setter
    def partidas(self, partidas):
        self.__partidas = partidas
