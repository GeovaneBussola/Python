numero = int(input('Digite um numero inteiro: '))

binario = ""
while numero != 0:
    r = numero % 2
    binario = str(r) + binario
    numero = numero // 2

print(binario)