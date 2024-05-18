# Entidade Equipe
from Aluno import Aluno

class Equipe():
    def __init__(self, nome: str, lista_alunos: list, pontos: int):
        self.__nome = nome
        self.__lista_alunos = [Aluno]
        self.__pontos = pontos
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def lista_alunos(self):
        return self.__lista_alunos
    
    @lista_alunos.setter
    def lista_alunos(self, lista_alunos):
        self.__lista_alunos = lista_alunos
    
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, pontos):
        self.__pontos
    
    def adicionar_aluno(self, lista_alunos):
        return
    
    def remover_aluno(self, lista_alunos):
        return
