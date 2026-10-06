def exemplo2(nome,tipo):
    arquivo= open(nome,tipo)
    arquivo.write('Kaua')
    arquivo.close()

    arquivo=open(nome,'r')
    print(arquivo.readline().strip())
    arquivo.close()


def exemplo3(nome,tipo):
    caminho_arquivo=nome
    arquivo=open(caminho_arquivo,tipo)
    linha1=arquivo.readline().strip()
    print(f'linha1: {linha1}')
    linha2=arquivo.readline().strip()
    print(f'linha 2: {linha2}')

    arquivo.close()



if __name__ =="__main__":
    caminho='/Users/aluno/Downloads/python/aula2/lendo_arquivo/dados.txt'
    modo=['w','r','x','a']


    exemplo2(caminho,modo[0])

    exemplo3(caminho,modo[1])



