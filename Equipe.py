# Entidade Equipe

from Aluno import Aluno
from Curso import Curso

class Equipe():
    def __init__(self, nome: str, curso: Curso, lista_alunos: list, pontos: int):
        self.__nome = nome
        self.__curso = curso
        self.__lista_alunos = [Aluno]
        self.__pontos = pontos = 0
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def curso(self, curso):
        self.__curso = curso
    
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
        self.__pontos = pontos
