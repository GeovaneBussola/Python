# 5- Criar um programa em Python que leia os dados necessários para cadastrar os nomes
# de N alunos em uma lista, em outra lista as respectivas notas dos alunos e em uma
# terceira lista o seu curso (ccp ou tads). Observe que na posição i das três listas ficarão
# guardados: o nome do aluno i, a nota do aluno i e o curso do aluno i.
# Resolva os seguintes itens:
# a) Calcule e visualize a quantidade de alunos do curso de tads.
# b) Calcule e visualize a média das notas dos N alunos.
# c) Quantos alunos estão com a nota acima da média.

alunos=[]
notas=[]
cursos=[]
alunos_tads=0
alunos_acima_da_media=0
print('Dgite nome, nota e o curso do aluno (ccp) ou (tads)')
while True:
    alunos.append(input('Nome: '))
    notas.append(float(input('Nota: ')))
    cursos.append(input('Curso (ccp) (tads): ').lower())
    sair = int(input('[0]Parar [1]Adiconar mais alunos'))
    if sair == 1:
        continue
    else:
        break
for i in cursos:
    if i == 'tads':
        alunos_tads+=1
media_alunos= sum(notas) / len(notas)
for i in notas:
    if i > media_alunos:
        alunos_acima_da_media+=1

print(f'Alunos matriculados em tads: [{alunos_tads}]')
print(f'Media alunos: [{media_alunos:.2f}]')
print(f'Alunos acima da média: [{alunos_acima_da_media}]')
