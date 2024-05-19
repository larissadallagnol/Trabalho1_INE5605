# Controlador Curso

from Curso import Curso
from TelaCurso import TelaCurso

class ControladorCurso():
    def __init__(self, controlador_sistema):
        self.__tela_curso = TelaCurso(self)
        self.__cursos = [Curso]
        self.__controlador_sistema = controlador_sistema

    def busca_curso_por_codigo(self, codigo: int):
        for curso in self.__cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def cadastrar_curso(self):
        dados_curso = self.__tela_curso.pega_dados_curso()
        existe_curso = False
        for curso in self.__cursos:
            if curso.codigo == dados_curso["codigo"]:
                existe_curso = True
        if existe_curso is False:
            novo_curso = Curso(dados_curso["codigo"], dados_curso["nome"])
            self.__cursos.append(novo_curso)

    def editar_curso(self):
        self.listar_cursos()
        codigo_curso = self.__tela_curso.seleciona_curso()
        curso = self.busca_curso_por_codigo(codigo_curso)

        if curso is not None:
            novos_dados_curso = self.__tela_curso.pega_dados_curso()
            curso.codigo = novos_dados_curso["codigo"]
            curso.nome = novos_dados_curso["nome"]
            self.listar_cursos()
        else:
            self.__tela_curso.mostra_mensagem("ATENCAO: Este curso nao existe")

    def excluir_curso(self):
        self.listar_cursos()
        codigo_curso = self.__tela_curso.seleciona_curso()
        curso = self.busca_curso_por_codigo(codigo_curso)

        if curso is not None:
            self.__cursos.remove(curso)
            self.listar_cursos()
        else:
            self.__tela_curso.mostra_mensagem("ATENCAO: Este curso nao existe")

    def listar_cursos(self):
        for curso in self.__cursos:
            self.__tela_curso.mostra_curso({"codigo": curso.codigo, "nome": curso.nome})

    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_curso, 2: self.editar_curso, 3: self.excluir_curso, 4: self.listar_cursos}
        while True:
            lista_opcoes[self.__tela_curso.mostra_tela_opcoes()]()
