def exemplo3():
    linhas=[
        "esta é a primeira vez q o kaua bonito escreve\n"
        "Esta é a segunda linha do kaua lindo\n"
        "Esta é a 3 linha do kaua lindo\n"
    ]
    with open("exemplo_writelines.txt","w",encoding="utf-8")as arquivo:
        arquivo.writelines(linhas)


    with open("exemplo_writelines.txt","r",encoding="utf-8")as arquivo:
        conteudo=arquivo.read()
        print("Conteudo do arquivo")
        print(conteudo)


if __name__ == "__main__":
    exemplo3()

