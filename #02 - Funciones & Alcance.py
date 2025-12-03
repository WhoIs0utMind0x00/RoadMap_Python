def uno_cien():
    for n in range(1, 101):
        print(n)
def multiplos():
    for n in range(1, 101):
        if n % 1 == 0:
            print(n)
        if n % 3 == 0:
            print(f"{n} es múltiplo de 3")
        if n % 5 == 0:
            print(f"{n} es múltiplo de 5")
        if n % 5 == 0 and n % 3 == 0:
            print(f"{n} es múltiplo de 3 y de 5")

multiplos()