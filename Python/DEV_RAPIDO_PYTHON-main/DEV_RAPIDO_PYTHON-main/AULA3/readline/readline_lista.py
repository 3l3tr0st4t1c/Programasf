def exemplo4(nome):
    #caminho='/Users/aluno/Downloads/python/readline/dados.txt'

    arquivo=open("dados.txt",'w')
    arquivo.write("Kaua")
    arquivo.writelines(["\nCaroline", "\nVanessa" , "\nCristina"])
    arquivo.close()

def criar(caminho):
    arquivo=open(caminho, 'r')
    linhas=arquivo.readline()
    for i, linha in enumerate(linhas,start=1):
        print(f'linha {i}: {linha}')


if __name__ =="__main__":
    caminho='/Users/aluno/Downloads/python/readline/dados.txt'
    exemplo4(caminho)
    

