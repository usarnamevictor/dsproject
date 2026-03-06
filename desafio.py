
# Exemplo de desafio: encontrar a palavra mais frequente em uma linha

entrada = input().split()

contagem = {}

for palavra in entrada:
    contagem[palavra] = contagem.get(palavra, 0) + 1

maior = 0
resultado = ""

for palavra in entrada:
    if contagem[palavra] > maior:
        maior = contagem[palavra]
        resultado = palavra

print(resultado)
