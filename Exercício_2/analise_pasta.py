import os
import csv
from matplotlib import pyplot as plt


def pede_pasta(pasta):
    print (os.listdir(pasta))

def faz_calculos(pasta):
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0  
    count4 = 0
    volume = 0
    volume1 = 0
    volume2 = 0
    volume3 = 0
    volume4 = 0
    dic_info = {'pdf': 0, 'xlsx': 0, 'png': 0, 'docx': 0, 'doc' : 0}

    for i in os.listdir(pasta):
        if(i.endswith(".xlsx")):
            count += 1
            if os.path.isfile(os.path.join(pasta,i)):
                volume = os.path.getsize(os.path.join(pasta, i))
            dic_info["xlsx"] = {'volume': volume, 'quantidade:': count}
        elif(i.endswith(".pdf")):
            count1 += 1
            if os.path.isfile(os.path.join(pasta,i)):
                volume1 = os.path.getsize(os.path.join(pasta, i))
            dic_info["pdf"] = {'volume': volume1, 'quantidade:': count1}
        elif(i.endswith(".png")):
            count2 += 1
            if os.path.isfile(os.path.join(pasta,i)):
                volume2 = os.path.getsize(os.path.join(pasta, i))
            dic_info["png"] = {'volume': volume2, 'quantidade:': count2}
        elif(i.endswith(".docx")):
            count3 += 1
            if os.path.isfile(os.path.join(pasta,i)):
                volume3 = os.path.getsize(os.path.join(pasta, i))
            dic_info["docx"] = {'volume': volume3, 'quantidade:': count3}
        elif(i.endswith(".doc")):
            count4+=1
            if os.path.isfile(os.path.join(pasta,i)):
                volume4 = os.path.getsize(os.path.join(pasta, i))
            dic_info["doc"] = {'volume': volume4, 'quantidade:': count4} 
        
    print(dic_info)

def guarda_resultados(nomeFicheiro):
    with open('nomeFicheiro.csv', 'w', newline='') as ficheiro:
        campos = ['Extensão', 'Quantidade', 'Tamanho']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        writer.writerow({'Extensão':'pdf', 'Quantidade': 3, 'Tamanho': 910053})
        writer.writerow({'Extensão': 'xlsx', 'Quantidade': 0, 'Tamanho': 0}) 
        writer.writerow({'Extensão': 'png', 'Quantidade': 0, 'Tamanho': 0})
        writer.writerow({'Extensão': 'docx', 'Quantidade': 1, 'Tamanho': 192008}) 
        writer.writerow({'Extensão': 'doc', 'Quantidade' : 4, 'Tamanho' : 64512})

def faz_grafico_queijos(titulo, lista_chaves, lista_valores):
    
    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()

def faz_grafico_barras(titulo, lista_chaves, lista_valores):
    
    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()


pede_pasta("C:\\Users\\mariisa\\OneDrive\\Ambiente de Trabalho\\Nova pasta")
faz_calculos("C:\\Users\\mariisa\\OneDrive\\Ambiente de Trabalho\\Nova pasta")
guarda_resultados("C:\\Users\\mariisa\\OneDrive\\Ambiente de Trabalho\\Nova pasta")