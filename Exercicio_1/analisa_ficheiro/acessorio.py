import json

def pede_nome(nomeFicheiro):
    if (nomeFicheiro[-4:] == '.txt'):
        print (f'{nomeFicheiro}')
    else :
        print (f'O ficheiro não existe')

pede_nome("historia.txt")

def gera_nome(nomeFicheiro):
    with open(nomeFicheiro'.json', 'w') as json_file:
        json.drump(nomeFicheiro, json_file)
        
gera_nome("historia.txt")