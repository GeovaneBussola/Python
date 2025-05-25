# Exercícios de fixação
# 1- Faça um método que receba como parâmetros o Km inicial, Km final, quantidade de
# litros gastos e preço do litro. Calcule e mostre:
# - Distância percorrida;
# - Consumo médio;
# - Valor gasto;
# Faça um programa principal que solicite para o usuário o valor da quilometragem inicial,
# final, a quantidade de litros gastos e o preço do litro e mostre a distância percorrida, o
# consumo médio e o valor gasto, para isso utilize o método definido acima.

def dcv(qinicial,qfinal,qlgasto,lpreço):
    distancia_percorrida = qfinal - qinicial
    consumo_medio = distancia_percorrida / qlgasto
    valor_gasto = qlgasto * lpreço
    print(f'Distancia percorrida: {distancia_percorrida}Km\nConsumo médio: {consumo_medio}km/l\nValor gasto: R${valor_gasto}')

vqinical = int(input('Digite o valor da quilometragem inical: '))
vqfinal = int(input('Digite o valor da quilometragem final: '))
qlgasto = float(input('Digite a quantidade de litros gastos: '))
lpreço = float(input('Digite o valor do litro da gasolina: '))
dcv(vqinical,vqfinal,qlgasto,lpreço)


