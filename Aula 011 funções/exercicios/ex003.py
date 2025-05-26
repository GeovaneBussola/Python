# 3- Construir um método que receba como parâmetros o valor de uma compra e a
# quantidade de parcelas e calcula e retorna o valor da parcela, sabendo que a loja
# acrescenta 5% de juros para as compras parceladas.
# No algoritmo principal, solicite para o usuário o valor de uma compra e a quantidade de
# parcelas e utilizando o método descrito acima, mostre o valor da parcela.


def calculo(vlcompra,qparcelas):
    vlparcela = vlcompra
    if qparcelas > 1 :
        vlparcela = (vlcompra * 1.05) / qparcelas
    return vlparcela
vlcompra = float(input('Digite o valor da compra: R$'))
qparcelas = int(input('Digite a quantidade de parcelas: '))
if qparcelas >1: print(f'O valor das parcelas é: R${calculo(vlcompra,qparcelas):.2f}')
else: print(f'O valor da parcela é: R${calculo(vlcompra,qparcelas):.2f}')