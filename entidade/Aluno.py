# Entidade Aluno

from entidade.abstractPessoa import AbstractPessoa
from entidade.curso import Curso
import datetime

class Aluno(AbstractPessoa):
    def __init__(self, nome: str, cpf :int, data_de_nascimento: datetime.date, matricula: str, curso: Curso):
        super().__init__(nome, cpf, data_de_nascimento)
        self.__matricula = matricula
        self.__curso = curso

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
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso
