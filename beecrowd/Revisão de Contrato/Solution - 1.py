#Durante anos, todos os contratos da Associação de Contratos da Modernolândia (ACM) foram datilografados em uma velha máquina de datilografia.
#Recentemente Sr. Miranda, um dos contadores da ACM, percebeu que a máquina apresentava falha em um, e apenas um,
# dos dígitos numéricos. Mais especificamente, o dígito falho, quando datilografado, não é impresso na folha,
# como se a tecla correspondente não tivesse sido pressionada. Ele percebeu que isso poderia ter alterado os valores numéricos representados nos contratos e,
# preocupado com a contabilidade, quer saber, a partir dos valores originais negociados nos contratos, que ele mantinha em anotações manuscritas,
# quais os valores de fato representados nos contratos. Por exemplo, se a máquina apresenta falha no dígito 5,
# o valor 1500 seria datilografado no contrato como 100, pois o 5 não seria impresso.
# Note que o Sr. Miranda quer saber o valor numérico representado no contrato, ou seja,
# nessa mesma máquina, o número 5000 corresponde ao valor numérico 0, e não 000 (como ele de fato aparece impresso).

a = input()
a = a.split(" ")
num = a[0]
fullNum = list(a[1])

while int(num) > 0 or int(a[1]) > 0:
    for i in range(fullNum.count(num)):
        fullNum.remove(num)

    if not len(fullNum):
        print("0")
    else:
        c = "".join(fullNum)
        print(int(c))

    a = input()
    a = a.split(" ")
    num = a[0]
    fullNum = list(a[1])