import sys

def pergunta_imc(imc):
    try:
        if imc > 24.9:
            raise ValueError
    except ValueError:
        print('Seu imc está acima do permitido, favor normalizar forma física e somente após isso responder o teste.')
        sys.exit()


imc = float(input('Digite seu imc: '))
pergunta_imc(imc)
altura = float(input('Digite sua altura: '))
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))

vezes = int(input('Quantas vezes você treina por semana? '))
minutos = int(input('Aproximadamente quantos minutos por sessão de treino? '))

try:
    min_treino = vezes * minutos
    if min_treino < 300:
        raise ValueError
except ValueError:
    print('Muito obrigado, agradecemos a sua participação!')
    sys.exit()


print('Parabéns, você passou em todos os nossos testes, agora você fará um teste pessoal em nossa sede, favor comparecer ao endereço: Rua dos Atletas, 43, Bairro do Futebol. Nos vemos lá!')