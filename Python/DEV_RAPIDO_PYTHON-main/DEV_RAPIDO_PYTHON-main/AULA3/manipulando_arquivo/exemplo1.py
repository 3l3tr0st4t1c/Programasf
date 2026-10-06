def exemplo1():
    arquivo=open('/Users/aluno/downloads/python/aula2/manipulando arquivo/dados.txt')

    print('Nome do arquivo',arquivo.name)
    print('Tamanho do arquivo (Bytes)',arquivo.tell())
    print('Modo arquivo',arquivo.mode)
    print('Arquivo está fechado ? ',arquivo.closed)

    arquivo.close()


    print('Arquivo está fechado ? ',arquivo.closed)
if __name__ =="__main__":
    exemplo1()


