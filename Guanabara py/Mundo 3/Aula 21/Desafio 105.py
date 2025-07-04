# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*notas,situação=False):
    dicionario=dict()
    dicionario['Quantidade de notas'] = len(notas)
    dicionario['Maior'] = max(notas)
    dicionario['Menor'] = min(notas)
    dicionario['Media'] = sum(notas) / len(notas)
    if situação == True:
        if dicionario['Media'] <5:
            dicionario['Situação'] = 'Ruim'
        elif dicionario['Media'] <7:
            dicionario['Situação'] = 'Rasuavel'
        else:
            dicionario['Situação'] = 'Boa'
    return dicionario

print(notas(3,7,4,3,7,situação=True))