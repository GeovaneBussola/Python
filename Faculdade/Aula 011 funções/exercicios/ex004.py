# 4- Elabore um programa para calcular a velocidade de três objetos diferentes (com
# velocidade constante).
# Conhecemos (são dados digitados pelo usuário), para cada objeto, a distância percorrida
# e o tempo que necessitou para percorrer essa distância.
# Utilize um método geral que calcule e retorne a velocidade de um objeto, fornecidos
# como parâmetros os dados de distância e tempo.

def calcula_velocidade(distancia,tempo):
    velocidade = distancia/tempo
    return velocidade
for i in range(1,4):
    objeto = input(f'Digite o nome do {i}° objeto: ')
    distancia = float(input('Digite a distancia percorrida em (km): '))
    tempo = float(input('Digite o tempo gasto em horas: '))
    print(f'A velocidade do(a) {objeto} é: {calcula_velocidade(distancia,tempo):.2f}')
