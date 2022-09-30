def lin():
    """
    Design de linha simples com 30 repetições
    :return: Sem retorno
    """
    print('-' * 30)


def voto(a):
    """
    Função para calcular a idade da pessoa para o programa de obrigatoriedade de voto.
    :param a: Seu ano de nascimento para calcular sua idade.
    :return: Sem retorno
    """
    from datetime import date
    idade = date.today().year - a
    if 18 <= idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    else:
        return f'Com {idade} anos: VOTO FACULTATIVO'


lin()
voto(int(input('Digite seu ano de nascimento: ')))
