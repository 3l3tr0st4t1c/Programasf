def sinonimos(dicio):
    for i in dicio:
        print(f"{i} sinonimo {dicio[i]}\n")


def adicionar_palavras(result):

    palavra = input(str("Digite uma nova palavra: ")).strip().lower()
    sinonimo_dela = input(str("Digite seu sinonimo: ")).strip().lower()

    if result.get(palavra):
        print("Ja existe essa palavra")
    else:
        for i in result:
            existe = result[i]

            if sinonimo_dela in existe:
                print("Ja existe esse sinonimo")
                return

        result[palavra] = [sinonimo_dela]

        print(f"{palavra} adicionada com sucesso  -> sinonimo: {sinonimo_dela}")


def buscar_sinonimos(dict):
    print("Bem vindo ao buscador, Palavras disponiveis para buscar a seguir : ")
    for i in dict:
        print(i)
    escolhida=input("Digite a palavra que deseja ver os sinonimos : ").strip().lower()
    if dict.get(escolhida):
                print(f"o Sinonimo de {escolhida} é  -> " , dict[escolhida])
    else:
        print(f"Nao achamos {escolhida} no dicionario ")

def remover_palavra(dicionario):
    print("Bem vindo ao removedor de palavras, palavras disponiveis:  ")
    for i in dicionario:
        print(i)
    remover=input("Digite o nome da palavra que quer remover:").strip().lower()
    if dicionario.get(remover):
        del dicionario[remover]
        print(f"Palavra removida com sucesso {remover}")
    else:
        print(f"Nao existe nenhuma palavra com nome {remover}")


        
            
        
if __name__ == "__main__":
    dicionario = {}

    while True:
        opcao = input("""
              MENU DE SINÔNIMOS

            1 - Ver Todos Sinonimos
            2 - Adicionar palavra
            3 - Buscar Sinonimo
            4 - Remover palavra
            5 - Sair 

        Digite uma opção: """)

        match opcao:
            case "1":
                sinonimos(dicionario)

            case "2":
                adicionar_palavras(dicionario)
            case "3":
                buscar_sinonimos(dicionario)
                
            case "4":
                remover_palavra(dicionario)
            case "5":
                break


        input("\nPressione Enter para continuar...")