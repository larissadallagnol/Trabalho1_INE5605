# classe abstrata - Pessoa

from abc import ABC, abstractmethod
import datetime

class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: int, data_de_nascimento: datetime.date):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_de_nascimento = data_de_nascimento

    @property
    @abstractmethod
    def nome(self) -> str:
        return self.__nome

    @property
    @abstractmethod
    def cpf(self) -> str:
        return self.__cpf

    @property
    @abstractmethod
    def data_de_nascimento(self) -> datetime.date:
        return self.__data_de_nascimento
