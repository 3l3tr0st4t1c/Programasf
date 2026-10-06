class Contato:
    def __init__(self, nome="", sobrenome="", email="", telefone=""):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

class ControleContatos:
    def __init__(self):
        self.dicionario={}

    def criar(self):
        with open("arquivo.txt","+",encoding="utf-8")as arquivo:
            arquivo.write(self.dicionario)


        with open("arquivo.txt","r",encoding="utf-8")as arquivo:
            conteudo=arquivo.read()
            print("Conteudo do arquivo")
            print(conteudo)

    

    def adicionar(self):
        nome=input("Digite o nome Do contato a adicionar:")
        sobrenome=input("Digite seu sobrenome:")
        email=input("Digite seu email:")
        telefone=input("Digite seu telefone:")

        if self.dicionario.get(email):
             print("Esse contato ja existe")
        else:
            novo_contato = Contato(nome, sobrenome, email, telefone)

            conteudo=self.dicionario[email]=novo_contato
            with open("arquivo.txt","r+",encoding="utf-8")as arquivo:
                 arquivo.write(conteudo)
                 print(conteudo)



        



    def buscar(self):
        with open("arquivo.txt","r",encoding="utf-8")as arquivo:
            achou=False
            print(arquivo)
            for emails,nomes in arquivo():
                print(nomes.nome)
        
        escolhido=input("Digite o nome do contato :").strip().lower()
        for emails,objeto_contato in arquivo():
             if escolhido == objeto_contato.nome.lower():
                  print(objeto_contato.nome,objeto_contato.telefone)
                  achou=True
        if achou == False:
            print(f"Nao foi possivel achar {escolhido}")

    def printar(self):
         with open("arquivo.txt","r",encoding="utf-8")as arquivo:
            for i,j in arquivo():
                print(f"Lista de contatos : ", j.nome, j.sobrenome ,j.telefone)

    def remover(self):
         achou=False
         chave_remover=""
         with open("arquivo.txt","r",encoding="utf-8")as arquivo:
            print("Lista de contatos para remover : ")
            for chave,contato in arquivo():
                print(contato.nome)
            retirar=input("Digite o nome do contato que deseja retirar:").strip().lower()
            for cara,excluido in self.dicionario.items():
                if retirar == excluido.nome.lower():
                    chave_remover=cara
                    achou=True
                    break
              
                 
         if achou ==False:
            print(f"Nao achamos {retirar} na lista de contatos")  

         if chave_remover != "":
            del self.dicionario[chave_remover]
            print(f"{retirar} retirado da lista de contatos com sucesso")
                      
        
             
        
        
             
        
if __name__ =="__main__":
    agenda=ControleContatos()
    while True:
            opcao = input("""
                  MENU CONTATOS
                1 - Ver Contatos
                2 - Adicionar Contato
                3 - Buscar Contato
                4 - Remover Contato
                5 - Sair
                
    
            Digite uma opção: """)
    
            match opcao:
            
                case "1":
                      agenda.printar()
                case "2":

                    agenda.adicionar()
                    for chave_email,objeto_contato in agenda.dicionario.items():
                            print(f"Chave {chave_email}")
                            print(f"Nome do contato guardado {objeto_contato.nome} {objeto_contato.sobrenome}")
                case "3":
                      agenda.buscar()
                case "4":
                      agenda.remover()
                case "5":
                      break
    
    
            input("\nPressione Enter para continuar...")
        
  


    
    
