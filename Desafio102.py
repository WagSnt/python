def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    :param n: O número que será calculado
    :param show: (OPCIONAL) se mostrará o a Equação
    :return: Retorna o valor do fatorial de "n"
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f



print(fatorial(5, True))
