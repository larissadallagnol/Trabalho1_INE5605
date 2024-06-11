# Entidade Curso
from entidade.equipe import Equipe

class Curso():
    def __init__(self, codigo: int, nome: str):
        self.__codigo = codigo
        self.__nome = nome
        self.__equipes = [Equipe]
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
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
