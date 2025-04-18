num = input('Digite um numero binario: ')
n = len(num) - 1
decimal = 0

for i in num:
    decimal = decimal + int(i)*2**n
    n = n - 1
print(decimal)