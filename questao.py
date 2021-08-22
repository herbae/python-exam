import random

class Questao:
    def __init__(self, pergunta, opcoes, respostaCorreta, alternativas) -> None:
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.respostaCorreta = respostaCorreta
        self.alternativas = alternativas

    def responder(self):
        resposta = ''
        while len(resposta) != 1 or resposta not in self.alternativas:
            resposta = input(f'\nSua resposta {self.alternativas}): ')
        
        return resposta == self.respostaCorreta

    def imprimir(self):
        self.imprimirPergunta()
        self.imprimirOpcoes()

    def imprimirPergunta(self):
        print(self.pergunta)

    def imprimirOpcoes(self):
        for i, o in enumerate(self.opcoes):
            print(f'{chr(i + 97)}) {o}')

class GeradorQuestao:
    def __init__(self, listaModelo) -> None:
        self.listaModelo = listaModelo

    def gerarQuestoes(self, numeroInicial, numeroFinal):
        return [(i, self.gerarQuestaoAleatoria(i)) for i in range(numeroInicial, numeroFinal + 1)]

    def gerarOpcoes(self, respostaCorreta, opcoesIncorretasValidas):
        opcoes = []
        opcaoCorreta = ''
        if random.randrange(5) == 0:
            opcoes = random.sample(opcoesIncorretasValidas, 4)
            opcaoCorreta = 'e'
        else:
            opcoes = random.sample(opcoesIncorretasValidas, 3) + [respostaCorreta]
            random.shuffle(opcoes)
            opcaoCorreta = chr(opcoes.index(respostaCorreta) + 97)
        
        opcoes.append('Nenhuma das anteriores')
        return opcoes, opcaoCorreta

    def gerarQuestaoAleatoria(self, numeroQuestao) -> Questao:
        modelo = self.selecionarModelo()
        listaVariaveis = modelo.criarVariaveisAleatorias()

        pergunta = modelo.textoPergunta % (numeroQuestao, *listaVariaveis)
        respostaCorreta = modelo.funcaoResultado(*listaVariaveis)
        opcoes, opcaoCorreta = self.gerarOpcoes(
            str(respostaCorreta),
            [o for o in modelo.opcoesValidas(*listaVariaveis) if str(o) != str(respostaCorreta)])

        return Questao(pergunta, opcoes, opcaoCorreta, 'a b c d e'.split(' '))
    
    def selecionarModelo(self):
        return self.listaModelo[random.randrange(0, len(self.listaModelo))]

class ModeloQuestao:
    def __init__(self, listaGeradorVariaveis, funcaoResultado, opcoesValidas, textoPergunta) -> None:
        self.textoPergunta = textoPergunta
        self.listaGeradorVariaveis = listaGeradorVariaveis
        self.funcaoResultado = funcaoResultado
        self.opcoesValidas = opcoesValidas

    def criarVariaveisAleatorias(self):
        return [v() for v in self.listaGeradorVariaveis]
