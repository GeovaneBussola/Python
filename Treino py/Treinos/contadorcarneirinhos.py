carneirinho = 0
while True:
    dormi = input('Ja dormi?: ').lower()
    if dormi == 'nao':
        carneirinho += 1
    else:
        print(carneirinho, "carneirinhos")
        break