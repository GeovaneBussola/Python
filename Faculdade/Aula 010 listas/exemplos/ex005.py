#Testando Função (def)

r1 = 0
def test1():
        global r1
        r1 += n1 + n2
def test2():
        global r1
        r1 += n1 - n2
while True:
    n1 = int(input('Digite n1: '))
    n2 = int(input('Digite n2: '))
    fazer = input('Digite o sinal')
    if fazer == "+":
        test1()
    elif fazer == "-":
        test2()
    chave = input('Digite:\n[0] Continuar\n[1] Parar')
    if chave == "0":
          continue
    elif chave == "1":
          break
print(f'O resultado total é {r1}')

