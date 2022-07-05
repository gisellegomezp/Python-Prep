def EsPrimo(valor):
    if (type(valor) != int):
            return None
    for i in range(2, (int(valor / 2) + 1)):
        if valor % i == 0:
            return False
    return True
EsPrimo(11)