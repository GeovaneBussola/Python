# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Corinthians.
def linhas():
    print('-' * 30)
brasileirao_2025 = (
    "Flamengo",
    "Cruzeiro",
    "Red Bull Bragantino",
    "Palmeiras",
    "Fluminense",
    "Botafogo",
    "Bahia",
    "Mirassol",
    "Atlético-MG",
    "Ceará",
    "Corinthians",
    "Grêmio",
    "São Paulo",
    "Internacional",
    "Vasco da Gama",
    "Vitória",
    "Fortaleza",
    "Santos",
    "Juventude",
    "Sport"
)
linhas()
print('Os 5 primeiros times do brasileirão são:')
for i in range(1,6):
    print(f'{brasileirao_2025[i-1]}')

linhas()
print('Os 4 últimos colocados são:')
for i in range(4):
    print(f'{brasileirao_2025[-4+i]}')

linhas()
print('Times em ordem alfabetica: ')
for i in sorted(brasileirao_2025):
    print(i)
    
linhas()
print(f'O Corinthians esta na {brasileirao_2025.index("Corinthians") + 1}° posição')

