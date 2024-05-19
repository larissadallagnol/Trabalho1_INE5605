# Controlador Campeonato

from Campeonato import Campeonato
from TelaCampeonato import TelaCampeonato
from ControladorEquipe import ControladorEquipe
from ControladorPartida import ControladorPartida

class ControladorCampeonato():
    def __init__(self, controlador_sistema):
        self.__tela_campeonato = TelaCampeonato(self)
        self.__campeonatos = [Campeonato]
        self.__controlador_sistema = controlador_sistema
    
    @property
    def campeonatos(self):
        return self.__campeonatos

    def busca_campeonato_por_nome(self, nome: str):
        for campeonato in self.__campeonatos:
            if campeonato.nome == nome:
                return campeonato
        return None
    
    def classificacao(self):
        return

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
                lista_equipes.append(ControladorEquipe.busca_equipe_por_nome(nome))
            lista_partidas = []
            numero_split = dados_campeonato["lista_partidas"].split()
            for numero in numero_split:
                lista_partidas.append(ControladorPartida.busca_partida_por_numero(numero))
            novo_campeonato = Campeonato(dados_campeonato["nome"], lista_equipes, lista_partidas)
            self.__campeonatos.append(novo_campeonato)

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
                lista_equipes.append(ControladorEquipe.busca_equipe_por_nome(nome))
            campeonato.equipes = lista_equipes
            lista_partidas = []
            numero_split = novos_dados_campeonato["lista_partidas"].split()
            for numero in numero_split:
                lista_partidas.append(ControladorPartida.busca_partida_por_numero(numero))
            campeonato.partidas = lista_partidas
            self.listar_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Este campeonato nao existe")

    def excluir_campeonato(self):
        self.listar_campeonatos()
        nome_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.busca_campeonato_por_nome(nome_campeonato)

        if campeonato is not None:
            self.__campeonatos.remove(campeonato)
            self.listar_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Este campeonato nao existe")

    def listar_campeonatos(self):
        for campeonato in self.__campeonatos:
            self.__tela_campeonato.mostra_campeonato({"nome": campeonato.nome, "equipes": campeonato.equipes, "partidas": campeonato.partidas})

    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_campeonato, 2: self.editar_campeonato, 3: self.excluir_campeonato, 4: self.listar_campeonatos}
        while True:
            lista_opcoes[self.__tela_campeonato.mostra_tela_opcoes()]()
