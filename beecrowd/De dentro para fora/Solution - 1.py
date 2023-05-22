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