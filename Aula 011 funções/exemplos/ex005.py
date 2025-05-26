# Exemplo 5 - Trigonometria
# Vamos criar um programa que calcule o seno, cosseno e a tangente a partir da entrada
# dos catetos oposto e adjacente de um triângulo retângulo. Para tanto, precisaremos de
# quatro métodos:
# • Cálculo da hipotenusa do triângulo:
# • Cálculo do seno e cosseno:
# • Cálculo da tangente:
# Faça um programa principal que solicite ao usuário o cateto oposto (catO) e o adjacente
# (catA) e, usando os métodos definidos acima, mostre o seno, cosseno e a tangente.
# Separe os métodos em um arquivo chamado trigonometria.py e não utilize o módulo
# math

def calculo_hipotenusa(catO,catA):
    hipotenusa= (catO**2+catA**2)**0.5
    return hipotenusa
def calculo_seno_e_cosseno(hipotenusa,catO,catA):
    senoA= catO / hipotenusa
    cossenoA= catA / hipotenusa
    return senoA,cossenoA
def calculo_tangente(senoA,cossenoA):
    tangenteA= senoA/cossenoA
    return tangenteA

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
seno,cosseno=calculo_seno_e_cosseno(calculo_hipotenusa(cateto_oposto,cateto_adjacente),cateto_oposto,cateto_adjacente)
tangente=calculo_tangente(seno,cosseno)

print(f'Seno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')