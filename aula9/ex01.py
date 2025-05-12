# 1- Elabore um programa em Python que solicite o e-mail do usuário e imprima na tela
# somente o domínio. Exemplo:
# Entre com seu e-mail: teste@uol.com.br
# O domínio do seu e-mail é: http://uol.com.br

email = input('Digite seu gmail: ').lstrip()
while '@' not in email:
    email = input('Digite um gmail valido: ').lstrip()
aroba= email.find('@')
print(f'O seu dominio é: http://{email[aroba +1:]}')