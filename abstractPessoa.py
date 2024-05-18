# classe abstrata - Pessoa

from abc import ABC, abstractmethod
import datetime

class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def nome(self) -> str:
        pass

    @property
    @abstractmethod
    def cpf(self) -> str:
        pass

    @property
    @abstractmethod
    def data_nascimento(self) -> datetime.date:
        pass

    @abstractmethod
    def alterar_nome(self, nome :str):
        pass

    @abstractmethod
    def alterar_cpf(self, cpf :str):
        pass

    @abstractmethod
    def alterar_data_nascimento(self, data_nascimento :datetime.date):
        pass

    @abstractmethod
    def busca_pessoa_cpf(self, cpf: str):
        pass
