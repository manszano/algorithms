#Uma sentença é chamada de dançante se sua primeira letra for maiúscula e cada letra subsequente for o oposto da letra anterior.
# Espaços devem ser ignorados ao determinar o case (minúsculo/maiúsculo) de uma letra. Por exemplo,
# "A b Cd" é uma sentença dançante porque a primeira letra ('A') é maiúscula, a próxima letra ('b') é minúscula, a próxima letra ('C') é maiúscula,
# e a próxima letra ('d') é minúscula.

while True:
    try:
        s = list(input().casefold())
        i = 0
        t = True
        while i < len(s):
            if s[i].isalpha():
                if t:
                    s[i] = s[i].capitalize()
                    t = False
                else:
                    s[i] = s[i].casefold()
                    t = True
            i += 1
        print("".join(s))
    except EOFError:
        break