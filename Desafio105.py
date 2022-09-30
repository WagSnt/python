def notas(*n, sit=False):
    """
    Calculadora para média da turma e situação atual das notas
    :param n: notas informadas pelo usuário
    :param sit: Situação baseada no cálculo da média geral da turma
    :return: Retorna mostrando a quantidade de notas, a menor nota, a maior nota, a média da turma e a situação.
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] > 7:
            r['Situação'] = 'Boa'
        if 6 <= r['Média'] <= 7:
            r['Situação'] = 'Razoável'
        elif r['Média'] < 6:
            r['Situação'] = 'Ruim'
    return r


resp = notas(3.5, 7.0, 6.5, 8.6, 10, sit=True)
print(resp)
