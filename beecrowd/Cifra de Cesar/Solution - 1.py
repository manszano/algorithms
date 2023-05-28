
while True:
    try:
        a = False
        b = False
        c = False
        d = False
        senha = input()
        if len(senha) < 6 or len(senha) > 32:
            print('senha invalida.')
            d = True

        for i in senha:
            if ord(i) > 127 or i == " " or i == ".":
                d = True
            else:
                if i.isdigit():
                    a = True
                elif i.isalpha() and i.isupper():
                    b = True
                elif i.isalpha() and i.islower():
                    c = True

        if a and b and c and not d:
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break
