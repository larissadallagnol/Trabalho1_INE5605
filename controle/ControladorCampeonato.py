# Controlador Campeonato

from entidade.campeonato import Campeonato
from limite.telaCampeonato import TelaCampeonato

class ControladorCampeonato():
    def __init__(self, controlador_sistema):
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonatos = []
        self.__controlador_sistema = controlador_sistema
    
    @property
    def campeonatos(self):
        return self.__campeonatos

    # Busca um cameponato pelo nome dele
    def busca_campeonato_por_nome(self, nome: str):
        for campeonato in self.__campeonatos:
            if campeonato.nome == nome:
                return campeonato
        return None
    
    # Define a classificacao do campeonato
    def classificacao(self):
        classificacao = {}
        return classificacao

    # Cadastra um novo campeonato
    def cadastrar_campeonato(self):
        dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
        existe_campeonato = False
        for campeonato in self.__campeonatos:
            if campeonato.nome == dados_campeonato["nome"]:
                existe_campeonato = True
        if existe_campeonato is False:
            lista_equipes = []
            nome_split = dados_campeonato["lista_equipes"].split()
            for nome in nome_split:
                lista_equipes.append(self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(nome))
            lista_partidas = []
            numero_split = dados_campeonato["lista_partidas"].split()
            for numero in numero_split:
                lista_partidas.append(self.__controlador_sistema.controlador_partida.busca_partida_por_numero(numero))
            novo_campeonato = Campeonato(dados_campeonato["nome"], lista_equipes, lista_partidas)
            self.__campeonatos.append(novo_campeonato)

    # Edita um campeonato existente
    def editar_campeonato(self):
        self.listar_campeonatos()
        nome_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.busca_campeonato_por_nome(nome_campeonato)

        if campeonato is not None:
            novos_dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
            campeonato.nome = novos_dados_campeonato["nome"]
            lista_equipes = []
            nome_split = novos_dados_campeonato["lista_equipes"].split()
            for nome in nome_split:
                lista_equipes.append(self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(nome))
            campeonato.equipes = lista_equipes
            lista_partidas = []
            numero_split = novos_dados_campeonato["lista_partidas"].split()
            for numero in numero_split:
                lista_partidas.append(self.__controlador_sistema.controlador_partida.busca_partida_por_numero(numero))
            campeonato.partidas = lista_partidas
            self.listar_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Este campeonato nao existe")

    # Exclui um campeonato existente
    def excluir_campeonato(self):
        self.listar_campeonatos()
        nome_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.busca_campeonato_por_nome(nome_campeonato)

        if campeonato is not None:
            self.__campeonatos.remove(campeonato)
            self.__tela_campeonato.mostra_mensagem("Campeonato excluido")
            self.listar_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Este campeonato nao existe")

    # Lista os campeonatos existentes
    def listar_campeonatos(self):
        if len(self.__campeonatos) != 0:
            for campeonato in self.__campeonatos:
                self.__tela_campeonato.mostra_campeonato({"nome": campeonato.nome, "equipes": campeonato.equipes, "partidas": campeonato.partidas})
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Ainda nao existem campeonatos")

    # Finaliza o uso do controlador e volta para o sistema principal
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    # Abre tela de opcoes
    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_campeonato, 2: self.editar_campeonato, 3: self.excluir_campeonato, 4: self.listar_campeonatos}
        while True:
            lista_opcoes[self.__tela_campeonato.mostra_tela_opcoes()]()
