import os 

def pede_pasta (pasta):
    pasta = str(input("Introduza o caminho da pasta que quer: "))

    if (os.path.exists(pasta)):
        print (pasta)
    else:
        while True:
            print (f'Introduza novamente o nome da pasta')  
            break  

def calcula_tamanho_pasta(pasta):
    soma = 0

    for i in os.listdir(pasta):
        if (os.path.isfile(os.path.join(pasta, i))):
            soma+=os.path.getsize(os.path.join(pasta, i)) / 2**20
        elif (os.path.dir(os.path.join(pasta, i))):
            soma+=os.path.getsize(os.path.join(pasta, i)) / 2**20
    
    print (f'A soma total das pastas e ficheiros é de {soma} Mbytes')

if __name__ == "__main__": 
    #testar funções
    pede_pasta("C:\\Users\\mariisa\\OneDrive\\Ambiente de Trabalho\\New folder")
    calcula_tamanho_pasta("C:\\Users\\mariisa\\OneDrive\\Ambiente de Trabalho\\New folder")