import json

def pede_nome(nomeFicheiro):
    nomeFicheiro = str(input("Introduza o o nome do Ficheiro que quer: "))

    if (nomeFicheiro[-4:] == '.txt'):
        print (f'{nomeFicheiro}')
    else :
        while True:
            print (f'O ficheiro não existe')
            break

def gera_nome(nomeFicheiro):
    historia_dict={}
    with open('historia.json', 'w') as json_file:
        json.dump(historia_dict, json_file, indent = 4)

#testas funções    
#pede_nome("historia.txt")
gera_nome("historia.txt")


