# Faça um programa em Python que solicite ao usuário uma quantidade de segundos,
# calcule e exiba a quantidade de horas, minutos e segundos.

segundos = int(input('Digite um valor em segundos: '))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto//60
restosegundos = resto% 60

print(f"{segundos} segundos equivalem a: {horas}h {minutos}m {restosegundos}s")
