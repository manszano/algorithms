#Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las.
#O processo é muito simples. São feitas três passadas em todo o texto.
#Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII:
#letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|'
#e assim sucessivamente. Na segunda passada, a linha deverá ser invertida.
#Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII.
#Neste caso, 'b' vira 'a' e 'a' vira '`'.

cases = int(input())


def first(s):
    for i in range(len(s)):
        if s[i].isupper() or s[i].islower():
            z = ord(s[i]) + 3
            s[i] = chr(z)
    return s


def second(x):
    x.reverse()
    return x


def third(c):
    y = round(len(c) / 2 - 0.1)
    for i in range(y, len(c)):
        b = ord(c[i]) - 1
        c[i] = chr(b)
    return c


for i in range(cases):
    a = list(input())
    first(a)
    second(a)
    third(a)
    print("".join(a))

