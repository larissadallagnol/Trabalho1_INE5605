# entidade Arbitro

from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa
import datetime

class Arbitro(AbstractPessoa, ABC):
    def __init__(self, nome: str, cpf :str, data_nascimento: datetime.date, numero_partidas: int):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
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
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    
    @property
    def numero_partidas(self):
        return self.__numero_partidas
    
    @numero_partidas.setter
    def numero_partidas(self, numero_partidas):
        self.__numero_partidas = numero_partidas

    '''def alterar_nome(self, novo_nome :str):
        novo_nome = input("Escreva o novo nome:", )
        self.nome = novo_nome
        return self.__nome

    def alterar_cpf(self, cpf :str):
        return

    def alterar_data_nascimento(self, data_nascimento :datetime.date):
        return

    def busca_pessoa_cpf(self, cpf: str):
        return

    def adicionar_partidas(self, numero_partidas: int):
        return'''
