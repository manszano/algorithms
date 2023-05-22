
#A sua impressora foi infectada por um vírus e está imprimindo de forma incorreta.
# Depois de olhar para várias páginas impressas por um tempo, você percebe que ele está imprimindo cada linha de dentro para fora.
# Em outras palavras, a metade esquerda de cada linha está sendo impressa a partir do meio da página até a margem esquerda.
# Do mesmo modo, a metade direita de cada linha está sendo impressa à partir da margem direita e prosseguindo em direção ao centro da página.

casos = int(input())

for caso in range(casos):
    s = list(input())
    size = (len(s) / 2)
    rev1 = []
    rev2 = []
    for i in range(len(s)-1,-1,-1):
        if i < size:
            rev1.append(s[i])
        else:
            rev2.append(s[i])
    print("".join(rev1) + "".join(rev2))
    rev1.clear()
    rev2.clear()