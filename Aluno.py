# entidade Aluno

from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa
from Curso import Curso
import datetime

class Aluno(AbstractPessoa, ABC):
    def __init__(self, nome: str, cpf :str, data_nascimento: datetime.date, matricula: str, curso_aluno: Curso):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.matricula = matricula
        self.curso_aluno = curso_aluno

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def curso_aluno(self):
        return self.__curso_aluno
    
    @curso_aluno.setter
    def curso_aluno(self, curso_aluno):
        self.__curso_aluno = curso_aluno

    def alterar_nome(self, novo_nome :str):
        novo_nome = input("Escreva o novo nome:", )
        self.nome = novo_nome
        return self.__nome

    def alterar_cpf(self, cpf :str):
        return

    def alterar_data_nascimento(self, data_nascimento :datetime.date):
        return
