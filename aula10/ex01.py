notas =[]
contadornota=1
for i in range(5):
    nota = float(input(f'Digite a {contadornota} nota: '))
    contadornota+=1
    notas.append(nota)
contador=0
media =0
for i in notas:
    media += i 
media = media / len(notas)
print(f'A media do aluno é: {media:.2f}')
