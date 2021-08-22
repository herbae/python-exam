from questao import *

## main
modelo1 = ModeloQuestao(
    [lambda: random.randrange(25), lambda: random.randrange(25)],
    lambda x, y: x + y,
    lambda *_: list(range(0, 50)),
'''
Questão %d: o que vai ser impresso quando o código abaixo for executado?

x = %d
y = %d
print(x + y)

''')

modelo2 = ModeloQuestao(
    [lambda: random.randrange(25), lambda: random.randrange(25)],
    lambda x, y: x - y,
    lambda *_: list(range(-25, 25)),
'''
Questão %d: o que vai ser impresso quando o código abaixo for executado?

x = %d
y = %d
print(x - y)

''')

modelo3 = ModeloQuestao(
    [lambda: random.randrange(25), lambda: random.randrange(5), lambda: random.randrange(5)],
    lambda x, y, z: x - y * z,
    lambda *_: list(range(-25, 25)),
'''
Questão %d: o que vai ser impresso quando o código abaixo for executado?

x = %d
y = %d
z = %d
print(x - y * z)

''')

modelo4 = ModeloQuestao(
    [lambda: random.randrange(2) == 1, lambda: random.randrange(2) == 1],
    lambda x, y: x and y,
    lambda *_: ['True', 'False', 'true', 'false', '0'],
'''
Questão %d: o que vai ser impresso quando o código abaixo for executado?

print(%s and %s)

''')

modelo5 = ModeloQuestao(
    [lambda: random.randrange(50) for _ in range(3)],
    lambda *lista: lista[1],
    lambda *lista: list(lista) + [-1, 0, 1, 'lista[1]'],
'''
Questão %d: o que vai ser impresso quando o código abaixo for executado?

lista = [%d, %d, %d]
print(lista[1])

''')

def resposta6(x, y, z, w):
    if x >= y:
        return 'Será impresso "Autorizado"'
    elif z <= w:
        return 'Será impresso "Não autorizado"'
    else:
        return 'Nada será impresso'

modelo6 = ModeloQuestao(
    [lambda: random.randrange(50) for _ in range(4)],
    resposta6,
    lambda *lista: list(map(lambda x: f'Será impresso {x}', lista)) +
        ['Será impresso "Autorizado"', 'Será impresso "Não autorizado"', 'Nada será impresso'],
'''
Questão %d: o que vai ser impresso quando o código abaixo for executado?

if %d >= %d:
    print('Autorizado')
elif %d <= %d:
    print('Não autorizado')

''')

print('Bem vindo ao Exame 1 de Python (beta)')

nomeAluno = input('Digite seu nome, caríssimo: ')

questoes = GeradorQuestao([modelo1, modelo2, modelo3]).gerarQuestoes(1, 5)
questoes += GeradorQuestao([modelo4, modelo5, modelo6]).gerarQuestoes(6, 10)

respostas = []
for q in questoes:
    q[1].imprimir()
    respostas.append((q[0], q[1].responder()))

print('Prova do aluno:', nomeAluno)
print('Resultado:\n', respostas)
p = len([r for r in respostas if r[1]]) / len(respostas) * 100
print(f'Acertou {p}%.')