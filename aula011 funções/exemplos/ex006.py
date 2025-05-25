# Exemplo 6 – Calculadora lambda
# Vamos criar uma calculadora simples que utilize a função lambda para realizar as
# operações de soma, subtração, divisão e multiplicação.
# Para tanto, criaremos uma estrutura como a apresentada abaixo:

soma = lambda a,b: a + b
subtracao = lambda a,b: a - b
multiplicacao = lambda a,b: a * b
divisao = lambda a,b: a / b

print('Calculadora lambda\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[0] Sair')
while True:
    operacao = int(input('Escolha uma operação: '))
    if operacao == 0: break
    elif str(operacao) not in "1234":
        print('Opção invalida')
        continue
    n1 = float(input('Digite primeiro numero: '))
    n2 = float(input('Digite segundo numero: '))
    if operacao == 1: print(soma(n1,n2))
        
    elif operacao == 2: print(subtracao(n1,n2))
        
    elif operacao == 3: print(multiplicacao(n1,n2))
        
    elif operacao == 4: print(divisao(n1,n2))
        
    
        