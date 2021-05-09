def pede_nome(nomeFicheiro):
    if (nomeFicheiro[-4:] == '.txt'):
        print (f'{nomeFicheiro}')
    else :
        print (f'O ficheiro não existe')

pede_nome("historia.txt")

def gera_nome(nomeFicheiro):
    nomeFicheiro.replace(".txt", ".json")
    print(nomeFicheiro)

gera_nome("historia.txt")