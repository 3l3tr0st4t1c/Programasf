def exemplo3():
    caminho_arquivo='/Users/aluno/Downloads/python/aula2/lendo_arquivo/dados.txt'

    arquivo=open(caminho_arquivo,'r')
    linhas=arquivo.readlines()

    for i, linha in enumerate(linhas,start=1):
        print(f'linha {i} : {linha}')


  


  
if __name__ =="__main__":
   
    exemplo3()


