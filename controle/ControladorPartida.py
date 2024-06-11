# Controlador Partida

from entidade.partida import Partida
from entidade.arbitro import Arbitro
from limite.telaPartida import TelaPartida
import datetime as dt
import random

class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__tela_partida = TelaPartida(self)
        self.__partidas = [Partida]
        self.__controlador_sistema = controlador_sistema
    
    @property
    def partidas(self):
        return self.__partidas
    
    @partidas.setter
    def partidas(self, partidas):
        self.__partidas = partidas

    # Busca uma partida pelo numero dela
    def busca_partida_por_numero(self, numero: str):
        for partida in self.__partidas:
            if partida.numero == numero:
                return partida
        return None
    
    # Acrescenta pontos a uma equipe
    def acrescentar_pontos(self, partida: Partida):
        if partida.__gols_primeira_equipe > partida.__gols_segunda_equipe:
            partida.__primeira_equipe.__pontos += 3
        elif partida.__gols_primeira_equipe == partida.__gols_segunda_equipe:
            partida.__primeira_equipe.__pontos += 1
            partida.__segunda_equipe.__pontos += 1
        else:
            partida.__segunda_equipe.__pontos += 3
    
    # Gera datas para as partidas
    def gera_data_partida(self):
        data_inicio_campeonato = '2024-06-01'
        data_fim_campeonato = '2024-12-31'
        delta = dt.datetime.strptime(data_fim_campeonato, '%Y-%m-%d') - dt.datetime.strptime(data_inicio_campeonato, '%Y-%m-%d')
        # Gera um numero aleatorio de dias dentro do intervalo
        random_dias = random.randint(0, delta.days)
        # Adiciona o numero aleatorio de dias na data de inicio do campeonato
        random_data = data_inicio_campeonato + dt.timedelta(days=random_dias)
        data_da_partida = random_data.strftime('%Y-%m-%d')
        return data_da_partida

    # Registra as partidas automaticamente a partir das equipes e arbitros existentes
    def registar_partidas(self, equipes: list, arbitro: Arbitro):
        numero_de_equipes = len(self.__controlador_sistema.controlador_equipe.equipes)
        numero_da_partida = 1
        for equipe in self.__controlador_sistema.controlador_equipe.equipes:
            equipes.append(equipe)
        
        for primeira_equipe in range(numero_de_equipes):
            for segunda_equipe in range(primeira_equipe + 1, numero_de_equipes):
                arbitro = random.choice(self.__controlador_sistema.controlador_arbitro.arbitros)
                self.__controlador_sistema.controlador_arbitro.adiciona_partida(arbitro)
                data = self.gera_data_partida()
                gols_primeira_equipe = random.randint(0, 10)
                gols_segunda_equipe = random.randint(0, 10)
                nova_partida = Partida(int(numero_da_partida), data, equipes[primeira_equipe], equipes[segunda_equipe], 
                                       arbitro, gols_primeira_equipe, gols_segunda_equipe)
                self.__partidas.append(nova_partida)
                self.acrescentar_pontos(nova_partida)
                self.__controlador_sistema.controlador_campeonato.classificacao()

    # Exclui uma partida existente
    def excluir_partida(self):
        self.listar_partidas()
        numero_partida = self.__tela_partida.seleciona_partida()
        partida = self.busca_partida_por_numero(numero_partida)

        if partida is not None:
            self.__partidas.remove(partida)
            self.__tela_partida.mostra_mensagem("Partida excluida")
            self.listar_partidas()
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Esta partida nao existe")

    # Lista as partidas existentes no campeonato
    def listar_partidas(self):
        if len(self.__partidas) != 0:
            for partida in self.__partidas:
                self.__tela_partida.mostra_partida({"numero": partida.numero, "data": partida.data, "primeira_equipe": partida.primeira_equipe, 
                                                    "segunda_equipe": partida.segunda_equipe, "arbitro": partida.arbitro, "gols_primeira_equipe": partida.gols_primeira_equipe, 
                                                    "gols_segunda_equipe": partida.gols_segunda_equipe})
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Ainda nao existem partidas")

    # Finaliza o uso do controlador e volta para o sistema principal
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    # Abre tela de opcoes
    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.registar_partidas, 2: self.excluir_partida, 3: self.listar_partidas}
        while True:
            lista_opcoes[self.__tela_partida.mostra_tela_opcoes()]()
