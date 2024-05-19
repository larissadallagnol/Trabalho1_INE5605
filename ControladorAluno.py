# Controlador Aluno

from Aluno import Aluno
from TelaAluno import TelaAluno

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__tela_aluno = TelaAluno(self)
        self.__alunos = [Aluno]
        self.__controlador_sistema = controlador_sistema

    def busca_aluno_por_cpf(self, cpf: int):
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                return aluno
        return None

    def cadastrar_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        existe_aluno = False
        for aluno in self.__alunos:
            if aluno.cpf == dados_aluno["cpf"]:
                existe_aluno = True
        if existe_aluno is False:
            novo_aluno = Aluno(dados_aluno["nome"], dados_aluno["cpf"], dados_aluno["data_de_nascimento"], dados_aluno["matricula"], dados_aluno["curso"])
            self.__alunos.append(novo_aluno)

    def editar_aluno(self):
        self.listar_alunos()
        cpf_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.busca_aluno_por_cpf(cpf_aluno)

        if aluno is not None:
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.cpf = novos_dados_aluno["cpf"]
            aluno.data_de_nascimento = novos_dados_aluno["data_de_nascimento"]
            aluno.matricula = novos_dados_aluno["matricula"]
            aluno.curso = novos_dados_aluno["curso"]
            self.listar_alunos()
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: Este aluno nao existe")

    def excluir_aluno(self):
        self.listar_alunos()
        cpf_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.busca_aluno_por_cpf(cpf_aluno)

        if aluno is not None:
            self.__alunos.remove(aluno)
            self.listar_alunos()
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: Este aluno nao existe")

    def listar_alunos(self):
        for aluno in self.__alunos:
            self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "data_de_nascimento": aluno.data_de_nascimento, "matricula": aluno.matricula, "curso": aluno.curso})

    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_aluno, 2: self.editar_aluno, 3: self.excluir_aluno, 4: self.listar_aluno}
        while True:
            lista_opcoes[self.__tela_aluno.mostra_tela_opcoes()]()
