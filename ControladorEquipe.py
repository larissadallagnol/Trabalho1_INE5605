# Controlador Equipe

from Equipe import Equipe
from TelaEquipe import TelaEquipe
from ControladorAluno import ControladorAluno
from ControladorCurso import ControladorCurso

class ControladorEquipe():
    def __init__(self, controlador_sistema):
        self.__tela_equipe = TelaEquipe(self)
        self.__equipes = [Equipe]
        self.__controlador_sistema = controlador_sistema

    @property
    def equipes(self):
        return self.__equipes

    def busca_equipe_por_nome(self, nome: str):
        for equipe in self.__equipes:
            if equipe.nome == nome:
                return equipe
        return None

    def cadastrar_equipe(self):
        dados_equipe = self.__tela_equipe.pega_dados_equipe()
        existe_equipe = False
        for equipe in self.__equipes:
            if equipe.nome == dados_equipe["nome"]:
                existe_equipe = True
        if existe_equipe is False:
            alunos_equipe = []
            cpf_split = dados_equipe["lista_alunos"].split()
            for cpf in cpf_split:
                aluno = ControladorAluno.busca_aluno_por_cpf(cpf)
                if aluno.curso == dados_equipe["curso"]:
                    alunos_equipe.append(aluno)
                else:
                    print("ATENCAO: Este aluno nao pertence ao curso da equipe")
            nova_equipe = Equipe(dados_equipe["nome"], dados_equipe["curso"], 
                                 alunos_equipe, dados_equipe["pontos"],)
            self.__equipes.append(nova_equipe)
            cursos = []
            for curso in ControladorCurso.cursos:
                if curso.equipes is "vazio":
                    print("ATENCAO: O curso %d está sem equipes!", curso)

    def editar_equipe(self):
        self.listar_equipes()
        nome_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.busca_equipe_por_nome(nome_equipe)

        if equipe is not None:
            novos_dados_equipe = self.__tela_equipe.pega_dados_equipe()
            equipe.nome = novos_dados_equipe["nome"]
            equipe.curso = novos_dados_equipe["curso"]
            alunos_equipe = []
            cpf_split = novos_dados_equipe["lista_alunos"].split()
            for cpf in cpf_split:
                aluno = ControladorAluno.busca_aluno_por_cpf(cpf)
                if aluno.curso == novos_dados_equipe["curso"]:
                    alunos_equipe.append(aluno)
                else:
                    print("ATENCAO: Este aluno nao pertence ao curso da equipe")
            equipe.lista_alunos = alunos_equipe
            self.listar_equipes()
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Esta equipe nao existe")

    def excluir_equipe(self):
        self.listar_equipes()
        nome_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.busca_equipe_por_nome(nome_equipe)

        if equipe is not None:
            self.__equipes.remove(equipe)
            self.listar_equipes()
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Esta equipe nao existe")

    def listar_equipes(self):
        for equipe in self.__equipes:
            self.__tela_equipe.mostra_equipe({"nome": equipe.nome, "curso": equipe.curso, 
                                              "lista_alunos": equipe.lista_alunos, "pontos": equipe.pontos})

    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_equipe, 2: self.editar_equipe, 
                        3: self.excluir_equipe, 4: self.listar_equipes}
        while True:
            lista_opcoes[self.__tela_equipe.mostra_tela_opcoes()]()
