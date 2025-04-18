binario = ""
decimal = int(input('Digite um numero decimal'))
while decimal != 0 : 
    if decimal % 2 == 0:
        binario = "0" + binario 
        decimal = decimal // 2
    else:
        binario = "1" + binario 
        decimal = decimal // 2

print(binario)
