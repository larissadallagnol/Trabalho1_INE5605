# Controlador Arbitro

from Arbitro import Arbitro
from TelaArbitro import TelaArbitro

class ControladorArbitro():
    def __init__(self, controlador_sistema):
        self.__tela_arbitro = TelaArbitro(self)
        self.__arbitros = [Arbitro]
        self.__controlador_sistema = controlador_sistema

    def busca_arbitro_por_cpf(self, cpf: int):
        for arbitro in self.__arbitros:
            if arbitro.cpf == cpf:
                return arbitro
        return None

    def cadastrar_arbitro(self):
        dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
        existe_arbitro = False
        for arbitro in self.__arbitros:
            if arbitro.cpf == dados_arbitro["cpf"]:
                existe_arbitro = True
        if existe_arbitro is False:
            novo_arbitro = Arbitro(dados_arbitro["nome"], dados_arbitro["cpf"], dados_arbitro["data_de_nascimento"], dados_arbitro["numero_partidas"])
            self.__arbitros.append(novo_arbitro)

    def editar_arbitro(self):
        self.listar_arbitros()
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.busca_arbitro_por_cpf(cpf_arbitro)

        if arbitro is not None:
            novos_dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
            arbitro.nome = novos_dados_arbitro["nome"]
            arbitro.cpf = novos_dados_arbitro["cpf"]
            arbitro.data_de_nascimento = novos_dados_arbitro["data_de_nascimento"]
            arbitro.numero_partidas = novos_dados_arbitro["numero_partidas"]
            self.listar_arbitros()
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Este arbitro nao existe")

    def excluir_arbitro(self):
        self.listar_arbitros()
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.busca_arbitro_por_cpf(cpf_arbitro)

        if arbitro is not None:
            self.__arbitros.remove(arbitro)
            self.listar_arbitros()
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Este arbitro nao existe")

    def listar_arbitros(self):
        for arbitro in self.__arbitros:
            self.__tela_arbitro.mostra_arbitro({"nome": arbitro.nome, "cpf": arbitro.cpf, "data_de_nascimento": arbitro.data_de_nascimento, "numero_partidas": arbitro.numero_partidas})

    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_arbitro, 2: self.editar_arbitro, 3: self.excluir_arbitro, 4: self.listar_arbitros}
        while True:
            lista_opcoes[self.__tela_arbitro.mostra_tela_opcoes()]()
