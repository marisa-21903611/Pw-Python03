def calcula_linhas(nomeFicheiro):
    f = open (nomeFicheiro)
    nomeFicheiro = f.read()
    f.close()

    count = 0
    for i in nomeFicheiro.split('\n'):
        count+=1
    print (f'Tem {count} linhas.')

#calcula_linhas("historia.txt")

def calcula_caracteres(nomeFicheiro):
    f = open (nomeFicheiro)
    nomeFicheiro = f.read()
    f.close()

    nomeFicheiro = nomeFicheiro.lower()

    count= 0
    for letra in nomeFicheiro:
        if (letra == 'a' or letra == 'b' or letra == 'c' or letra == 'd' or letra == 'e' or letra == 'f' or letra == 'g' 
        or letra == 'h' or letra == 'i' or letra == 'j' or letra == 'k' or letra == 'l' or letra == 'm' or letra == 'n'
        or letra == 'o' or letra == 'p' or letra == 'q' or letra == 'r' or letra == 's' or letra == 't' or letra == 'u'
        or letra == 'v' or letra == 'w' or letra == 'x' or letra == 'y' or letra == 'z'):
            count+=1
    print (f'O ficheiro tem {count} caracteres.')

#calcula_caracteres("historia.txt")

def calcula_palavra_comprida(nomeFicheiro):
    f = open (nomeFicheiro)
    nomeFicheiro = f.read()
    f.close()

    palavraComprida = nomeFicheiro.split()[0]

    for palavra in nomeFicheiro:
        if(palavra > palavraComprida):
            palavraComprida = palavra
    print(f'A palavra mais comprida do ficheiro é {palavraComprida}')

calcula_palavra_comprida("historia.txt")

def calcula_ocorrencias_de_letras(nomeFicheiro):
    f = open (nomeFicheiro)
    nomeFicheiro = f.read()
    f.close()

    nomeFicheiro = nomeFicheiro.lower()

    dicionario={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,
    'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

    for letra in nomeFicheiro:
        if (letra == 'a'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'b'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'c'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'd'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'e'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'f'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'g'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'h'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'i'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'j'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'k'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'l'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'm'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'n'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'o'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'p'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'q'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'r'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 's'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 't'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'u'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'v'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'w'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'x'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'y'):
            dicionario[letra]=dicionario[letra]+1
        elif (letra == 'z'):
            dicionario[letra]=dicionario[letra]+1

    print(dicionario)

#calcula_ocorrencias_de_letras("historia.txt")