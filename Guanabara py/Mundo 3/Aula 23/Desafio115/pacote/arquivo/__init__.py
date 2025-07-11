from pacote.interface import cabeçalho

def arquivoexiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(arquivo):
    try:
        a = open(arquivo,'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        print('Arquivo criado com sucesso')

def lerarquivo(arquivo):
    try:
        a = open(arquivo,'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        cabeçalho('Pessoas cadastradas')
        for i in a:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        a.close()

def cadastrar(arquivo,nome='desconhecido',idade=0):
    try:
        a = open(arquivo,'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escrita do arquivo')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()