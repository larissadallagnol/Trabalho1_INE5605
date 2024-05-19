# Entidade Arbitro

from abstractPessoa import AbstractPessoa
import datetime

class Arbitro(AbstractPessoa):
    def __init__(self, nome: str, cpf :str, data_de_nascimento: datetime.date, numero_partidas: int):
        super().__init__(nome, cpf, data_de_nascimento)
        self.__numero_partidas = numero_partidas

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
        return self.__data_nascimento
    
    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento
    
    @property
    def numero_partidas(self):
        return self.__numero_partidas
    
    @numero_partidas.setter
    def numero_partidas(self, numero_partidas):
        self.__numero_partidas = numero_partidas
