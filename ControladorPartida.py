# Controlador Partida

from Partida import Partida
from Arbitro import Arbitro
from TelaPartida import TelaPartida
from ControladorEquipe import ControladorEquipe
from ControladorArbitro import ControladorArbitro
from ControladorCampeonato import ControladorCampeonato
import datetime as dt
import random

class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__tela_partida = TelaPartida(self)
        self.__partidas = [Partida]
        self.__controlador_sistema = controlador_sistema

    def busca_partida_por_numero(self, numero: str):
        for partida in self.__partidas:
            if partida.numero == numero:
                return partida
        return None
    
    def acrescentar_pontos(self, partida: Partida):
        if partida.__gols_primeira_equipe > partida.__gols_segunda_equipe:
            partida.__primeira_equipe.__pontos += 3
        elif partida.__gols_primeira_equipe == partida.__gols_segunda_equipe:
            partida.__primeira_equipe.__pontos += 1
            partida.__segunda_equipe.__pontos += 1
        else:
            partida.__segunda_equipe.__pontos += 3
    
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

    def registar_partidas(self, equipes: list, arbitro: Arbitro):
        numero_de_equipes = len(ControladorEquipe.equipes)
        numero_da_partida = 1
        for equipe in ControladorEquipe.equipes:
            equipes.append(equipe)

        for primeira_equipe in range(numero_de_equipes):
            for segunda_equipe in range(primeira_equipe + 1, numero_de_equipes):
                arbitro = random.choice(ControladorArbitro.arbitros)
                ControladorArbitro.adiciona_partida(arbitro)
                data = self.gera_data_partida()
                gols_primeira_equipe = random.randint(0, 10)
                gols_segunda_equipe = random.randint(0, 10)
                nova_partida = Partida(int(numero_da_partida), data, equipes[primeira_equipe], equipes[segunda_equipe], arbitro, gols_primeira_equipe, gols_segunda_equipe)
                self.__partidas.append(nova_partida)
                self.acrescentar_pontos(nova_partida)
                ControladorCampeonato.classificacao()

    def excluir_partida(self):
        self.listar_partidas()
        numero_partida = self.__tela_partida.seleciona_partida()
        partida = self.busca_partida_por_numero(numero_partida)

        if partida is not None:
            self.__partidas.remove(partida)
            self.listar_partidas()
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Esta partida nao existe")

    def listar_partidas(self):
        for partida in self.__partidas:
            self.__tela_partida.mostra_partida({"numero": partida.numero, "data": partida.data, "primeira_equipe": partida.primeira_equipe, "segunda_equipe": partida.segunda_equipe, "arbitro": partida.arbitro, "gols_primeira_equipe": partida.gols_primeira_equipe, "gols_segunda_equipe": partida.gols_segunda_equipe})

    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.registar_partidas, 2: self.excluir_partida, 3: self.listar_partidas}
        while True:
            lista_opcoes[self.__tela_partida.mostra_tela_opcoes()]()
